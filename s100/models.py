from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.contrib.gis.db import models


class ISO639_3(models.TextChoices):
    FRENCH = "fra"
    ENGLISH = "eng"


class CodeList(models.TextChoices):
    """
    We may add "other" choices to this enum based on SHOM feedback.
    This is allowed by the spec by prefixing them with "other: ".
    r"other: [a-zA-Z0-9]+( [a-zA-Z0-9]+)*"
    """

    # In spec: A type of flexible enumeration.
    # A code list type is a list of literals which may be extended only in conformance with specified rules.


class GMSurface(models.PolygonField):
    """
    It should also include CurvePolygonField but Django does not support it.
    """


class GMMultiSurface(models.MultiPolygonField):
    # https://github.com/betagouv/SPPNautInterface/issues/229
    """
    It should also include MutliCurvePolygonField but Django does not support it.
    """


class ComplexAttributeType(models.Model):
    class Meta:
        abstract = True


class GenericComplexAttributeType(ComplexAttributeType):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.BigIntegerField()
    content_object = GenericForeignKey()

    class Meta:
        abstract = True


class FeatureName(GenericComplexAttributeType):
    # Language is not mandatory in the spec. We think it's because the language can be defined once at the XML root level and then is implied.
    # We make it mandatory because we need to know explicitly.
    language = models.CharField(max_length=3, choices=ISO639_3.choices)

    name = models.CharField(
        max_length=255, help_text="The individual name of a feature."
    )

    # Indication: Boolean. A True value is an indication that the name is intended to be displayed.
    # Remarks:
    # Where it is allowable to encode multiple instances of feature name for a single feature instance,
    # only one feature name instance can indicate that the name is to be displayed (display name set to True).
    display_name = models.BooleanField(
        default=False,
        help_text="A statement expressing if a feature name is to be displayed in certain display settings or not.",
    )

    def __str__(self):
        return f"{self.name} ({'✓ ' if self.display_name else ''}{self.language})"

    class Meta:
        constraints = [
            # https://github.com/betagouv/SPPNautInterface/issues/227
            models.UniqueConstraint(
                fields=["content_type", "object_id", "display_name"],
                condition=models.Q(display_name=True),
                name="unique_display_name",
            ),
            models.UniqueConstraint(
                fields=["content_type", "name", "language"],
                name="unique_name_per_feature_type_and_language",
            ),
        ]

        # Uncomment when upgrading to django 4.2
        # db_table_comment = "The complex attribute provides the name of an entity, "
        # "defines the national language of the name, and provides the option to "
        # "display the name at various system display settings."


class Information(GenericComplexAttributeType):
    language = models.CharField(max_length=3, choices=ISO639_3.choices)
    headline = models.CharField(max_length=255, blank=True)
    text = models.TextField(blank=True)

    def __str__(self):
        return f"{self.language} - {self.headline}"


class TextContent(GenericComplexAttributeType):
    class CategoryOfText(models.TextChoices):
        """
        Classification of completeness of textual information in relation to the
        source.
        """

        ABSTRACT_OR_SUMMARY = "abstract or summary"  # A statement summarizing the important points of a text.
        EXTRACT = "extract"  # An excerpt or excerpts from a text.
        FULL_TEXT = "full text"  # The whole text

    category_of_text = models.CharField(max_length=255, choices=CategoryOfText.choices)
    information = GenericRelation(Information)


class FeatureType(models.Model):
    feature_names = GenericRelation(FeatureName)
    text_contents = GenericRelation(TextContent)

    class Meta:
        abstract = True

    def __str__(self):
        if self.pk and (
            feature_name := self.feature_names.order_by("-display_name").first()
        ):
            return str(feature_name)

        return super().__str__()


class InformationType(models.Model):
    feature_names = GenericRelation(FeatureName)

    class Meta:
        abstract = True

    def __str__(self):
        if self.pk and (
            feature_name := self.feature_names.order_by("-display_name").first()
        ):
            return str(feature_name)

        return super().__str__()


class GenericManyToMany(models.Model):
    class Meta:
        abstract = True
