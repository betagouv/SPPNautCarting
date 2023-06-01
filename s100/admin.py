import nested_admin
from django.contrib.contenttypes.models import ContentType

import s100.models


class FeatureNameInline(nested_admin.NestedGenericTabularInline):
    model = s100.models.FeatureName
    is_sortable = False
    min_num = 1
    extra = 0


class InformationInline(nested_admin.NestedGenericStackedInline):
    model = s100.models.Information
    fields = ("headline", "text")
    # FIXME: Why did we decide to make it a 1 when the spec says [0..*] ?
    extra = 0
    min_num = 1
    max_num = 1
    is_sortable = False


class TextContentInline(nested_admin.NestedGenericStackedInline):
    model = s100.models.TextContent
    inlines = [InformationInline]
    extra = 0
    max_num = 1
    is_sortable = False
    # classes = ["collapse"] FIXME
