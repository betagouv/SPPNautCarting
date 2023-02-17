from __future__ import annotations

import logging
from functools import cached_property
from typing import NamedTuple
from xml.etree import ElementTree

import lxml.etree as ET
from django.contrib.gis.db import models
from django.core.serializers import serialize
from django.utils.safestring import mark_safe
from tree_queries.models import TreeNode, TreeQuerySet
from tree_queries.query import TreeManager

xslt_transform = ET.XSLT(ET.parse("carting/xslt/in_section_html.xslt"))


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
    TOPONYME = "TOPONYME", "texte/principal"
    REFERENCE = "REFERENCE", "texte/reference"

    def ingester(self) -> type[SectionIngester]:
        to_ingester = {
            self.OUVRAGE: OuvrageIngester,
            self.CHAPTER: ParagraphIngester,
            self.SUBCHAPTER: ParagraphIngester,
            self.PARAGRAPH: ParagraphIngester,
            self.SUBPARAGRAPH: ParagraphIngester,
            self.SUBSUBPARAGRAPH: ParagraphIngester,
            self.ALINEA: AlineaIngester,
            # FIXME: Ne devrait-on pas avoir un autre numéro ?
            self.TABLE: FigureIngester,
            self.ILLUSTRATION: FigureIngester,
            self.TOPONYME: SectionIngester,
            self.REFERENCE: SectionIngester,
        }
        return to_ingester[self]


class OuvrageSectionManager(models.Manager):
    def ingest_xml_subtree(
        self,
        ouvrage_name: str,
        element: ElementTree.Element,
        ouvrage_section: OuvrageSection | None = None,
    ) -> int:
        ingested = 0
        for typology in SectionTypology:
            for child_element in element.iterfind(typology.label):
                child_ouvrage_section = OuvrageSection.from_xml(
                    child_element, ouvrage_section, typology, ouvrage_name
                )
                child_ouvrage_section.save(
                    update_fields=(
                        "numero",
                        "content",
                        "typology",
                        "ouvrage_name",
                    )
                )

                logging.warning(
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

    # FIXME: À tester : peut-on retrouver dans le XML uniquement avec bpn_id
    bpn_id = models.UUIDField(editable=False, primary_key=True)
    numero = models.CharField(max_length=20, editable=False)
    content = models.TextField(editable=False)
    typology = models.CharField(
        max_length=25, choices=SectionTypology.choices, editable=False
    )
    # FIXME: Est-ce qu'on peut/veut en faire un field qui va chercher le root?
    # FIXME: Peut-être une entité ouvrage?
    ouvrage_name = models.CharField(max_length=10, editable=False)
    # FIXME: Valider la géométrie ?
    # geos.geometry.GEOSGeometry.valid
    geometry = models.GeometryField(null=True, blank=True, default=None, srid=4326)

    # FIXME: Unique_together ouvrage_name/typology/numero
    class Meta:
        # FIXME: ordering = ("ouvrage_name", "numero",)
        ordering = ("numero",)

    def __str__(self):
        return f"{self.numero} - {SectionTypology[self.typology].label}"

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

    def geojson(self):
        return serialize("geojson", [self], fields=("geometry",))

    @cached_property
    def content_html(self):
        if not self.content:
            return ""
        # FIXME: Remove before merging
        xslt_transform = ET.XSLT(ET.parse("carting/xslt/in_section_html.xslt"))

        return mark_safe(xslt_transform(ET.fromstring(self.content)))


class SectionIngester(NamedTuple):
    element: ElementTree.Element
    ouvrage_name: str

    # FIXME: Illustrations
    def numero(self, parent: OuvrageSection) -> str:
        return parent.numero

    def content(self) -> str:
        return ElementTree.tostring(self.element, encoding="unicode")


class AlineaIngester(SectionIngester):
    def numero(self, parent: OuvrageSection) -> str:
        # FIXME: 0. Peut-être plus utile avec l'arborescence?
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
