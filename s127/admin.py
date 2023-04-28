import nested_admin
from django.apps import AppConfig
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.contrib.gis.admin import GISModelAdmin

import s100.models
from carting.widgets import CustomOSMWidget

from . import models


# FIXME : move in a shared module, core or carting maybe ?
class GISModelAdminWithRasterMarine(GISModelAdmin):
    gis_widget = CustomOSMWidget


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
    model = models.VesselsMeasurements
    extra = 0


class ApplicabilityInline(nested_admin.NestedGenericStackedInline):
    model = models.Applicability
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


@admin.register(models.Applicability)
class ApplicabilityAdmin(nested_admin.NestedModelAdmin):
    search_fields = ["id"]
    inlines = [InformationInline, VesselsMeasurementsInline]


class FeatureTypePermissionTypeInline(nested_admin.NestedGenericTabularInline):
    ct_field = "feature_content_type"
    ct_fk_field = "feature_object_id"
    model = models.PermissionType

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
    search_fields = ["id"]


@admin.register(models.PilotService)
class PilotServiceAdmin(GISModelAdmin, FeatureTypeAdmin):
    fieldsets = [
        (
            "SPECIFIC FIELDS",
            {
                "fields": [
                    "geometry",
                    "pilotage_district",
                    "category_of_pilot",
                    "pilot_qualification",
                    "pilot_request",
                    "remote_pilot",
                ],
            },
        )
    ]
    autocomplete_fields = ["pilotage_district"]


@admin.register(models.PilotBoardingPlace)
class PilotBoardingPlaceAdmin(GISModelAdmin, FeatureTypeAdmin):
    pass
