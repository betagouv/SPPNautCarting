from functools import cached_property

import lxml.etree as ET
from django.contrib.gis.db import models
from django.core.serializers import serialize
from django.utils.safestring import mark_safe

xslt_transform = ET.XSLT(ET.parse("carting/document.xslt"))


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


class INSection(models.Model):

    bpn_id = models.CharField(max_length=40, unique=True)
    numero = models.CharField(max_length=20, null=True, blank=True, default=None)
    content = models.TextField(null=True, blank=True, default=None)
    typology = models.CharField(
        max_length=25,
        choices=SectionTypology.choices,
        null=True,
        blank=True,  # fixme : do we need it ?
        default=None,
    )
    xpath = models.CharField(max_length=512)
    ouvrage_name = models.CharField(max_length=10)
    # FIXME: Valider la géométrie ?
    # geos.geometry.GEOSGeometry.valid
    geometry = models.GeometryField(null=True, blank=True, default=None, srid=4326)

    def __str__(self):
        return f"{self.numero} - {self.typology}"

    def json(self):
        return serialize("geojson", [self], fields=("geometry",))

    @cached_property
    def content_html(self):

        if not self.content:
            return ""
        xslt_transform = ET.XSLT(ET.parse("carting/document.xslt"))

        return mark_safe(xslt_transform(ET.fromstring(self.content)))
