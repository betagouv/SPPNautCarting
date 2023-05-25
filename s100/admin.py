import nested_admin

import s100.models


class FeatureNameInline(nested_admin.NestedGenericTabularInline):
    model = s100.models.FeatureName
    extra = 1
    # FIXME overwrite get_extra to expose only one form when it is empty


class InformationInline(nested_admin.NestedGenericStackedInline):
    model = s100.models.Information
    fields = ("headline", "text")
    extra = 0
    min_num = 1
    max_num = 1


class TextContentInline(nested_admin.NestedGenericStackedInline):
    model = s100.models.TextContent
    inlines = [InformationInline]
    extra = 0
    max_num = 1
    # classes = ["collapse"] FIXME
