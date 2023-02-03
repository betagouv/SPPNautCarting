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
    TOPONYME = "TOPONYME", "principal"
    TABLE = "TABLE", "tableau"
    ILLUSTRATION = "ILLUSTRATION", "illustration"


# Create your models here.
class Element(models.Model):

    bpn_id = models.CharField(max_length=40, primary_key=True)
    numero = models.CharField(max_length=20, null=True, blank=True, default=None)
    content = models.TextField(null=True, blank=True, default=None)
    typology = models.CharField(
        max_length=25,
        choices=ElementTypology.choices,
        null=True,
        blank=True,  # fixme : do we need it ?
        default=None,
    )
    xpath = models.CharField(max_length=512)
    ouvrage_name = models.CharField(max_length=10)
    geometry = models.GeometryField(null=True, blank=True, default=None, srid=4326)

    def __str__(self):
        return f"{self.numero} - {self.bpn_id} - {self.typology} - {self.xpath}"
