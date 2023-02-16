from functools import cached_property
from xml.etree import ElementTree

import lxml.etree as ET
from django.contrib.gis.db import models
from django.core.serializers import serialize
from django.utils.safestring import mark_safe
from tree_queries.models import TreeNode

xslt_transform = ET.XSLT(ET.parse("carting/xslt/in_section_html.xslt"))


class SectionTypology(models.TextChoices):
    OUVRAGE = "OUVRAGE", "ouvrage"
    CHAPTER = "CHAPTER", "chapitre"
    SUBCHAPTER = "SUBCHAPTER", "sChapitre"
    PARAGRAPH = "PARAGRAPH", "para"
    SUBPARAGRAPH = "SUBPARAGRAPH", "sPara"
    SUBSUBPARAGRAPH = "SUBSUBPARAGRAPH", "ssPara"
    ALINEA = "ALINEA", "alinea"
    REFERENCE = "REFERENCE", "texte/reference"
    TOPONYME = "TOPONYME", "texte/principal"
    TABLE = "TABLE", "tableau"
    ILLUSTRATION = "ILLUSTRATION", "illustration"


# class Alinea(INSection):
#     class Meta:
#         pas_de_table = True


class INSection(TreeNode):
    bpn_id = models.UUIDField(editable=False, primary_key=True)
    numero = models.CharField(max_length=20, null=True, blank=True, default=None)
    content = models.TextField(null=True, blank=True, default=None)
    typology = models.CharField(
        max_length=25,
        choices=SectionTypology.choices,
        null=True,
        blank=True,  # fixme : do we need it ?
        default=None,
    )
    ouvrage_name = models.CharField(max_length=10)
    # FIXME: Valider la géométrie ?
    # geos.geometry.GEOSGeometry.valid
    geometry = models.GeometryField(null=True, blank=True, default=None, srid=4326)

    def __str__(self):
        return f"{self.numero} - {SectionTypology[self.typology].label}"

    @classmethod
    def from_xml(
        cls,
        element: ElementTree.Element,
        parent: "INSection",
        typology: SectionTypology,
    ):
        bpn_id = element.attrib["bpn_id"]

        if typology == SectionTypology.ALINEA:
            numero = f"{parent.numero}0.{element.find('nmrAlinea').text}"
        elif typology in [
            SectionTypology.TABLE,
            SectionTypology.ILLUSTRATION,
            SectionTypology.TOPONYME,
            SectionTypology.OUVRAGE,
            SectionTypology.REFERENCE,
        ]:
            numero = parent.numero
        else:
            numero = f"{parent.ouvrage_name}/{element.find('titre/numero').text}"

        if typology == SectionTypology.OUVRAGE:
            content = ""
        elif typology in [
            SectionTypology.CHAPTER,
            SectionTypology.SUBCHAPTER,
            SectionTypology.PARAGRAPH,
            SectionTypology.SUBPARAGRAPH,
            SectionTypology.SUBSUBPARAGRAPH,
        ]:
            titre = element.find("titre")
            content = ElementTree.tostring(titre, encoding="unicode")
        else:
            content = ElementTree.tostring(element, encoding="unicode")

        return cls(
            bpn_id=bpn_id,
            numero=numero,
            content=content,
            typology=typology,
            ouvrage_name=parent.ouvrage_name,
        )

    def json(self):
        return serialize("geojson", [self], fields=("geometry",))

    @cached_property
    def content_html(self):
        if not self.content:
            return ""
        xslt_transform = ET.XSLT(ET.parse("carting/xslt/in_section_html.xslt"))

        return mark_safe(xslt_transform(ET.fromstring(self.content)))
