import logging

import nested_admin
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.contrib.gis.admin import GISModelAdmin
from django.urls import reverse
from django.utils.html import format_html_join
from tree_queries.models import TreeNode

from .models import carting, s100, s127
from .widgets import CustomOSMWidget

logger = logging.getLogger(__name__)


def children(instance: TreeNode):
    children = instance.children.all()

    if not children:
        return "No children"

    return format_html_join(
        ", ",
        '<a href="{}">{}</a>',
        (
            (
                reverse(
                    f"admin:{instance._meta.app_label}_{instance._meta.model_name}_change",
                    args=(child.pk,),
                ),
                child,
            )
            for child in children
        ),
    )


@admin.register(carting.OuvrageSection)
class OuvrageSectionAdmin(GISModelAdmin):
    gis_widget = CustomOSMWidget
    ordering = ("numero",)
    list_display = ("__str__", "bpn_id", "ouvrage_name")
    list_filter = (
        ("geometry", admin.EmptyFieldListFilter),
        "typology",
    )
    search_fields = ("bpn_id", "numero", "content")

    readonly_fields = (
        "bpn_id",
        "numero",
        "content",
        children,
        "parent",
    )
    fields = (
        "numero",
        "bpn_id",
        "parent",
        children,
        "geometry",
        "content",
    )

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class FeatureNameInline(nested_admin.NestedGenericTabularInline):
    model = s100.FeatureName
    extra = 0
    min_num = 1
    max_num = 1


class InformationInline(nested_admin.NestedGenericStackedInline):
    model = s100.Information
    fields = ("headline", "text")
    extra = 0
    min_num = 1
    max_num = 1


class TextContentInline(nested_admin.NestedGenericStackedInline):
    model = s100.TextContent
    inlines = [InformationInline]
    extra = 0
    max_num = 1


class VesselsMeasurementsInline(nested_admin.NestedStackedInline):
    model = s127.VesselsMeasurements
    extra = 0


class ApplicabilityInline(nested_admin.NestedGenericStackedInline):
    model = s127.Applicability
    inlines = [InformationInline, VesselsMeasurementsInline]
    extra = 0
    # fieldsets = [
    #     (
    #         "GENERALITES",
    #         {
    #             "fields": ["in_ballast"],
    #         },
    #     ),
    #     (
    #         "DANGERS",
    #         {
    #             "fields": ["category_of_dangerous_or_hazardous_cargo"],
    #         },
    #     ),
    # ]


@admin.register(s127.Applicability)
class ApplicabilityAdmin(nested_admin.NestedModelAdmin):
    search_fields = ["id"]
    inlines = [InformationInline, VesselsMeasurementsInline]


class FeatureTypePermissionTypeInline(nested_admin.NestedGenericTabularInline):
    ct_field = "feature_content_type"
    ct_fk_field = "feature_object_id"
    model = s127.PermissionType

    min_num = 0
    extra = 0
    autocomplete_fields = ["applicability"]


class FeatureTypeAdmin(nested_admin.NestedModelAdmin):
    inlines = [
        FeatureNameInline,
        FeatureTypePermissionTypeInline,
        TextContentInline,
    ]


@admin.register(s127.PilotageDistrict)
class PilotageDistrictAdmin(GISModelAdmin, FeatureTypeAdmin):
    fieldsets = [
        (
            "SPECIFIC FIELDS",
            {
                "fields": ["geometry", "communication_channel"],
            },
        ),
    ]


@admin.register(s127.PilotService)
class PilotServiceAdmin(GISModelAdmin, FeatureTypeAdmin):
    pass


@admin.register(s127.PilotBoardingPlace)
class PilotBoardingPlaceAdmin(GISModelAdmin, FeatureTypeAdmin):
    pass
