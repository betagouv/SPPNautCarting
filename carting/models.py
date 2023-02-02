from django.contrib.gis.db import models


class ElementTypology(models.TextChoices):
    OUVRAGE = "OUVRAGE", "ouvrage"
    CHAPTER = "CHAPTER", "chapitre"
    SUBCHAPTER = "SUBCHAPTER", "sChapitre"
    PARAGRAPH = "PARAGRAPH", "para"
    SUBPARAGRAPH = "SUBPARAGRAPH", "sPara"
    SUBSUBPARAGRAPH = "SUBSUBPARAGRAPH", "ssPara"
    ALINEA = "ALINEA", "alinea"
    REFERENCE = "REFERENCE", "reference"
    TOPONYME = "TOPONYME", "primaire"
    TABLE = "TABLE", "tableau"


# Create your models here.
class Element(models.Model):

    bpn_id = models.CharField(max_length=32)
    content = models.TextField(null=True, blank=True, default=None)
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
    geometry = models.GeometryField(null=True, blank=True, default=None, srid=4326)

    def __str__(self):
        return f"{self.bpn_id} - {self.typology} - {self.xpath}"
