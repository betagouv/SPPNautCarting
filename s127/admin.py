import nested_admin
from django.apps import AppConfig
from django.contrib import admin

from carting.admin import GISModelAdminWithRasterMarine
from s100.admin import FeatureNameInline, InformationInline, TextContentInline

from . import models


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
