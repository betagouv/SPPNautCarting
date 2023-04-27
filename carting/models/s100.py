from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.contrib.gis.db import models


class ISO639_3(models.TextChoices):
    FRA = "fra", "French"
    ENG = "eng", "English"


class CategoryOfText(models.TextChoices):
    """
    Classification of completeness of textual information in relation to the
    source.

    :cvar ABSTRACT_OR_SUMMARY: A statement summarizing the important
        points of a text.
    :cvar EXTRACT: An excerpt or excerpts from a text.
    :cvar FULL_TEXT: The whole text
    """

    ABSTRACT_OR_SUMMARY = "abstract or summary"
    EXTRACT = "extract"
    FULL_TEXT = "full text"


class ComplexAttributeType(models.Model):
    class Meta:
        abstract = True


class GenericComplexAttributeType(ComplexAttributeType):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.BigIntegerField()
    content_object = GenericForeignKey()

    class Meta:
        abstract = True


# class GMLObject(models.Model):
#     # FIXME : Discuter de l'algo de création automatique de l'id
#     id = models.CharField(primary_key=True, max_length=255)


class FeatureName(GenericComplexAttributeType):
    language = models.CharField(
        max_length=3,
        choices=ISO639_3.choices,
    )
    name = models.CharField(
        max_length=255, help_text="The individual name of a feature."
    )
    display_name = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.language} - {self.name}"

    # Uncomment when upgrading to django 4.2
    # class Meta:
    #     db_table_comment = "The complex attribute provides the name of an entity, "
    #     "defines the national language of the name, and provides the option to "
    #     "display the name at various system display settings."


class Information(GenericComplexAttributeType):
    language = models.CharField(
        max_length=3, choices=ISO639_3.choices, default=ISO639_3.FRA
    )
    headline = models.CharField(max_length=255, blank=True)
    text = models.TextField(blank=True)


class TextContent(GenericComplexAttributeType):
    category_of_text = models.CharField(max_length=255, choices=CategoryOfText.choices)
    information = GenericRelation(Information)


class FeatureType(models.Model):
    feature_names = GenericRelation(FeatureName)
    text_contents = GenericRelation(TextContent)
    permission_types = GenericRelation("carting.PermissionType")

    class Meta:
        abstract = True


class InformationType(models.Model):
    feature_names = GenericRelation(FeatureName)

    class Meta:
        abstract = True
