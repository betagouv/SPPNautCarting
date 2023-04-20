from django.contrib.contenttypes.fields import (GenericForeignKey,
                                                GenericRelation)
from django.contrib.contenttypes.models import ContentType
from django.contrib.gis.db import models


class ISO639_3(models.TextChoices):
    FRA = "FRA"
    ENG = "ENG"


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


# class GMLObject(models.Model):
#     # FIXME : Discuter de l'algo de création automatique de l'id
#     id = models.CharField(primary_key=True, max_length=255)


class FeatureName(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.BigIntegerField()
    feature_type = GenericForeignKey()
    language = models.CharField(
        max_length=3,
        blank=True,
        null=True,
        choices=ISO639_3.choices,
        help_text="The language is encoded by a character code following ISO 639-3",
    )
    name = models.CharField(
        max_length=255, help_text="The individual name of a feature."
    )
    display_name = models.BooleanField(default=False)

    # Uncomment when upgrading to django 4.2
    # class Meta:
    #     db_table_comment = "The complex attribute provides the name of an entity, "
    #     "defines the national language of the name, and provides the option to "
    #     "display the name at various system display settings."


class TextContent(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.BigIntegerField()
    feature_type = GenericForeignKey()
    category_of_text = models.CharField(max_length=255, choices=CategoryOfText.choices)

class Information(models.Model):
    text_content = models.ForeignKey(
        TextContent, on_delete=models.CASCADE, related_name="information"
    )
    language = models.CharField(
        max_length=3,
        blank=True,
        null=True,
        choices=ISO639_3.choices,
        help_text="The language is encoded by a character code following ISO 639-3",
    )
    headline = models.CharField(max_length=255, blank=True)
    text = models.CharField(max_length=255, blank=True)
    # file_locator = models.CharField(max_length=255, blank=True)
    # file_reference = models.CharField(max_length=255, blank=True)


class FeatureType(models.Model):
    feature_names = GenericRelation(FeatureName)
    text_contents = GenericRelation(TextContent)

    class Meta:
        abstract = True
