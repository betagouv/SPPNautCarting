import nested_admin
from django.apps import AppConfig
from django.contrib import admin

import s100.models
from carting.admin import GISModelAdminWithRasterMarine

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
    model = models.VesselsMeasurements
    extra = 0


class ApplicabilityInline(nested_admin.NestedGenericStackedInline):
    model = models.Applicability
    inlines = [InformationInline, VesselsMeasurementsInline]
    extra = 0


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
class PilotageDistrictAdmin(GISModelAdminWithRasterMarine, FeatureTypeAdmin):
    search_fields = ["id"]


@admin.register(models.PilotService)
class PilotServiceAdmin(GISModelAdminWithRasterMarine, FeatureTypeAdmin):
    autocomplete_fields = ["pilotage_district"]


@admin.register(models.PilotBoardingPlace)
class PilotBoardingPlaceAdmin(GISModelAdminWithRasterMarine, FeatureTypeAdmin):
    pass
