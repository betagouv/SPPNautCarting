import nested_admin
from django.contrib.contenttypes.models import ContentType

import s100.models


class OneExtraWhenEmptyMixin:
    def get_extra(self, request, obj=None, **kwargs):
        if not obj:
            return 1

        related_content_type = ContentType.objects.get_for_model(obj)
        plop = self.model.objects.filter(
            content_type__pk=related_content_type.pk, object_id=obj.pk
        )
        if plop.count():
            return 0
        return 1


class FeatureNameInline(
    OneExtraWhenEmptyMixin, nested_admin.NestedGenericTabularInline
):
    model = s100.models.FeatureName


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
