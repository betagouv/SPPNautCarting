import nested_admin
from django.apps import AppConfig
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.contrib.gis.admin import GISModelAdmin

import s100.models

from . import models


class S100Config(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "s100"


class FeatureNameInline(nested_admin.NestedGenericTabularInline):
    model = s100.models.FeatureName
    extra = 0
    min_num = 1
    max_num = 1


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


class VesselsMeasurementsInline(nested_admin.NestedStackedInline):
    model = models.S127VesselsMeasurements
    extra = 0


class ApplicabilityInline(nested_admin.NestedGenericStackedInline):
    model = models.S127Applicability
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


@admin.register(models.S127Applicability)
class ApplicabilityAdmin(nested_admin.NestedModelAdmin):
    search_fields = ["id"]
    inlines = [InformationInline, VesselsMeasurementsInline]


class FeatureTypePermissionTypeInline(nested_admin.NestedGenericTabularInline):
    ct_field = "feature_content_type"
    ct_fk_field = "feature_object_id"
    model = models.S127PermissionType

    min_num = 0
    extra = 0
    autocomplete_fields = ["applicability"]


class FeatureTypeAdmin(nested_admin.NestedModelAdmin):
    inlines = [
        FeatureNameInline,
        FeatureTypePermissionTypeInline,
        TextContentInline,
    ]


@admin.register(models.PilotageDistrict)
class PilotageDistrictAdmin(GISModelAdmin, FeatureTypeAdmin):
    fieldsets = [
        (
            "SPECIFIC FIELDS",
            {
                "fields": ["geometry", "communication_channel"],
            },
        ),
    ]


@admin.register(models.S127PilotService)
class PilotServiceAdmin(GISModelAdmin, FeatureTypeAdmin):
    pass


@admin.register(models.S127PilotBoardingPlace)
class PilotBoardingPlaceAdmin(GISModelAdmin, FeatureTypeAdmin):
    pass
