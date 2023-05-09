from django.contrib.contenttypes.admin import GenericStackedInline, GenericTabularInline

import s100.models


class FeatureNameInline(GenericTabularInline):
    model = s100.models.FeatureName
    extra = 0
    min_num = 1
    max_num = 1


class InformationInline(GenericStackedInline):
    model = s100.models.Information
    fields = ("headline", "text")
    extra = 0
    min_num = 1
    max_num = 1


class TextContentInline(GenericStackedInline):
    model = s100.models.TextContent
    inlines = [InformationInline]
    extra = 0
    max_num = 1
