from __future__ import annotations

import itertools
import logging
from functools import cached_property
from typing import NamedTuple
from xml.etree import ElementTree

import lxml.etree as ET
from django.contrib.gis.db import models
from django.core.serializers import serialize
from django.db import DatabaseError
from django.utils.safestring import mark_safe
from tree_queries.models import TreeNode, TreeQuerySet

xslt_transform = ET.XSLT(ET.parse("carting/xslt/ouvrage_section_html.xslt"))


class SectionTypology(models.TextChoices):
    OUVRAGE = "OUVRAGE", "ouvrage"
    CHAPTER = "CHAPTER", "chapitre"
    SUBCHAPTER = "SUBCHAPTER", "sChapitre"
    PARAGRAPH = "PARAGRAPH", "para"
    SUBPARAGRAPH = "SUBPARAGRAPH", "sPara"
    SUBSUBPARAGRAPH = "SUBSUBPARAGRAPH", "ssPara"
    ALINEA = "ALINEA", "alinea"
    TABLE = "TABLE", "tableau"
    ILLUSTRATION = "ILLUSTRATION", "illustration"
    TOPONYME = "TOPONYME", "texte/principal|liste/texte/principal"
    REFERENCE = "REFERENCE", "texte/reference|liste/texte/reference"

    def ingester(self) -> type[SectionIngester]:
        to_ingester = {
            self.OUVRAGE: OuvrageIngester,
            self.CHAPTER: ParagraphIngester,
            self.SUBCHAPTER: ParagraphIngester,
            self.PARAGRAPH: ParagraphIngester,
            self.SUBPARAGRAPH: ParagraphIngester,
            self.SUBSUBPARAGRAPH: ParagraphIngester,
            self.ALINEA: AlineaIngester,
            self.TABLE: FigureIngester,
            self.ILLUSTRATION: FigureIngester,
            self.TOPONYME: SectionIngester,
            self.REFERENCE: SectionIngester,
        }
        return to_ingester[self]

    def iterable(self, element):
        for xpath in self.label.split("|"):
            yield from element.iterfind(xpath)

    def tag_name(self) -> str | None:
        to_tag_name = {
            self.CHAPTER: "h2",
            self.SUBCHAPTER: "h3",
            self.PARAGRAPH: "h4",
            self.SUBPARAGRAPH: "h5",
            self.SUBSUBPARAGRAPH: "h6",
        }
        return to_tag_name.get(self, None)


class OuvrageSectionManager(models.Manager):
    def ingest_xml_subtree(
        self,
        ouvrage_name: str,
        element: ElementTree.Element,
        ouvrage_section: OuvrageSection | None = None,
    ) -> int:
        ingested = 0
        for typology in SectionTypology:
            for child_element in typology.iterable(element):
                child_ouvrage_section = OuvrageSection.from_xml(
                    child_element, ouvrage_section, typology, ouvrage_name
                )
                child_ouvrage_section.ingest()

                logging.info(
                    "Section %s ingérée avec l'id %s",
                    typology.label,
                    child_ouvrage_section.bpn_id,
                )
                ingested += 1
                ingested += self.ingest_xml_subtree(
                    ouvrage_name, child_element, child_ouvrage_section
                )
        return ingested


class OuvrageSection(TreeNode):
    objects = OuvrageSectionManager.from_queryset(TreeQuerySet)()

    bpn_id = models.UUIDField(primary_key=True)
    numero = models.CharField(max_length=20)
    content = models.TextField(blank=True)
    typology = models.CharField(max_length=25, choices=SectionTypology.choices)
    ouvrage_name = models.CharField(max_length=10)
    geometry = models.GeometryField(blank=True, null=True, default=None, srid=4326)

    class Meta:
        ordering = ("numero",)

    def __str__(self):
        return f"{self.numero} - {SectionTypology[self.typology].name}"

    @classmethod
    def from_xml(
        cls,
        element: ElementTree.Element,
        parent: "OuvrageSection" | None,
        typology: SectionTypology,
        ouvrage_name: str,
    ) -> "OuvrageSection":
        ingester = typology.ingester()(element, ouvrage_name)

        return cls(
            bpn_id=element.attrib["bpn_id"],
            numero=ingester.numero(parent),
            content=ingester.content(),
            typology=typology,
            ouvrage_name=ouvrage_name,
            parent=parent,
        )

    def ingest(self):
        self.clean_fields()

        try:
            # This raises if the instance does not exist
            self.save(
                update_fields=(
                    "numero",
                    "content",
                    "typology",
                    "ouvrage_name",
                    "parent",
                )
            )
        except DatabaseError:
            self.save()

    def geojson(self) -> str | None:
        if not self.geometry:
            return None
        return serialize("geojson", [self], fields=("geometry",))

    @cached_property
    def content_html(self):
        if not self.content:
            return ""

        inner_html = xslt_transform(ET.fromstring(self.content))

        tag_name = SectionTypology[self.typology].tag_name()

        if tag_name:
            # FIXME : extraire dans un templatetag django
            inner_html = f'<{tag_name} class="fr-mt-2w">{inner_html}</{tag_name}>'
        return mark_safe(inner_html)

    @property
    def should_display(self):
        return self.typology not in [
            SectionTypology.REFERENCE,
            SectionTypology.TOPONYME,
        ]


class SectionIngester(NamedTuple):
    element: ElementTree.Element
    ouvrage_name: str

    def numero(self, parent: OuvrageSection) -> str:
        return parent.numero

    def content(self) -> str:
        return ElementTree.tostring(self.element, encoding="unicode")


class AlineaIngester(SectionIngester):
    def numero(self, parent: OuvrageSection) -> str:
        return f"{parent.numero}0.{self.element.find('nmrAlinea').text}"


class FigureIngester(SectionIngester):
    def numero(self, parent: OuvrageSection) -> str:
        return self.element.find("numero").text


class ParagraphIngester(SectionIngester):
    def numero(self, parent: OuvrageSection) -> str:
        return self.element.find("titre/numero").text

    def content(self) -> str:
        return ElementTree.tostring(self.element.find("titre"), encoding="unicode")


class OuvrageIngester(SectionIngester):
    def numero(self, parent: None) -> str:
        return self.ouvrage_name

    def content(self) -> str:
        return ""
