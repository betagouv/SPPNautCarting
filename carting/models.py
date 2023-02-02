from django.contrib.gis import forms
from django.contrib.gis.db import models

from carting.widgets import CustomOSMWidget2


class OSMGeometryFormField(forms.GeometryField):
    widget = CustomOSMWidget2
    pass


class OSMGeometryField(models.GeometryField):
    form_class = OSMGeometryFormField


# Create your models here.
class Element(models.Model):
    class ElementTypology(models.TextChoices):
        OUVRAGE = "OUVRAGE", "Ouvrage"
        CHAPTER = "CHAPTER", "Chapter"
        SUBCHAPTER = "SUBCHAPTER", "Sub chapter"
        PARAGRAPH = "PARAGRAPH", "Paragraph"
        SUBPARAGRAPH = "SUBPARAGRAPH", "SubParagraph"
        SUBSUBPARAGRAPH = "SUBSUBPARAGRAPH", "SubSubParagraph"
        ALINEA = "ALINEA", "Alinea"
        REFERENCE = "REFERENCE", "Reference"
        TOPONYME = "TOPONYME", "Topomyne"
        TABLE = "TABLE", "Table"

    bpn_id = models.CharField(max_length=32)
    content = models.TextField()
    typology = models.CharField(
        max_length=255,
        choices=ElementTypology.choices,
        null=True,
        blank=True,  # fixme : do we need it ?
        default=None,
    )
    xpath = models.CharField(
        max_length=511
    )  # fixme : 512-1, is it the right convention ?
    geometry = OSMGeometryField(null=True, blank=True, default=None, srid=4326)

    def __str__(self):
        return f"{self.bpn_id} - {self.typology} - {self.xpath}"
