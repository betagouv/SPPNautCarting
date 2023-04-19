from django.contrib.gis.db import models


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


class GMLObject(models.Model):
    id = models.CharField(primary_key=True, max_length=255)


class FeatureType(GMLObject):
    pass


class FeatureName(models.Model):
    feature_type = models.ForeignKey(
        "carting.FeatureType",
        on_delete=models.CASCADE,
        null=True,
        related_name="feature_name",
        help_text="",
    )
    display_name = models.BooleanField(default=False)
    language = models.CharField(
        # FIXME : add choices with available languages
        max_length=3,
        blank=True,
        null=True,
        help_text="The language is encoded by a character code following ISO 639-3",
    )
    name = models.CharField(
        max_length=255, help_text="The individual name of a feature."
    )

    # Uncomment when upgrading to django 4.2
    # class Meta:
    #     db_table_comment = "The complex attribute provides the name of an entity, "
    #     "defines the national language of the name, and provides the option to "
    #     "display the name at various system display settings."


class TextContent(models.Model):
    feature_type = models.ForeignKey(
        "carting.FeatureType",
        on_delete=models.CASCADE,
        null=True,
        related_name="text_content",
        help_text="",
    )
    category_of_text = models.CharField(max_length=255, choices=CategoryOfText.choices)


class Information(models.Model):
    text_content = models.ForeignKey(
        "carting.TextContent", on_delete=models.CASCADE, related_name="information"
    )
    headline = models.CharField(max_length=255, blank=True)
    language = models.CharField(
        # FIXME : add choices with available languages
        max_length=3,
        blank=True,
        null=True,
        help_text="The language is encoded by a character code following ISO 639-3",
    )
    text = models.CharField(max_length=255, blank=True)
    # file_locator = models.CharField(max_length=255, blank=True)
    # file_reference = models.CharField(max_length=255, blank=True)
