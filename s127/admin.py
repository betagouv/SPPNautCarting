import nested_admin
from django.contrib import admin

import s127
from carting.admin import GISModelAdminWithRasterMarine, ModelAdminWithOrderedFormsets
from s100.admin import FeatureNameInline, InformationInline, TextContentInline


class VesselsMeasurementsInline(nested_admin.NestedStackedInline):
    model = s127.models.VesselsMeasurements
    extra = 0


class ApplicabilityInline(nested_admin.NestedGenericStackedInline):
    model = s127.models.Applicability
    inlines = [InformationInline, VesselsMeasurementsInline]
    extra = 0


class ContactAddressInline(admin.StackedInline):
    model = s127.models.ContactAddress
    extra = 0


class TelecommunicationsInline(admin.StackedInline):
    model = s127.models.Telecommunications
    extra = 1


@admin.register(s127.models.ContactDetails)
class ContactDetailsAdmin(admin.ModelAdmin):
    search_fields = ["id"]
    inlines = [TelecommunicationsInline, ContactAddressInline, InformationInline]


class PilotBoardingPlaceInline(nested_admin.NestedStackedInline):
    inlines = [FeatureNameInline]
    model = s127.models.PilotBoardingPlace
    extra = 0


class SrvContactInline(nested_admin.NestedGenericTabularInline):
    ct_field = "feature_content_type"
    ct_fk_field = "feature_object_id"
    model = s127.models.SrvContact

    min_num = 0
    extra = 0
    autocomplete_fields = ["contact_details"]


class FeatureTypePermissionTypeInline(nested_admin.NestedGenericTabularInline):
    ct_field = "feature_content_type"
    ct_fk_field = "feature_object_id"
    model = s127.models.PermissionType

    min_num = 0
    extra = 0
    autocomplete_fields = ["applicability"]


class FeatureTypeInlinesMixin:
    inlines = [
        FeatureNameInline,
        FeatureTypePermissionTypeInline,
        TextContentInline,
    ]


class FeatureTypeAdmin(FeatureTypeInlinesMixin, nested_admin.NestedModelAdmin):
    pass


class FeatureTypeInline(FeatureTypeInlinesMixin, nested_admin.NestedStackedInline):
    pass


class PilotServiceInlineMixin:
    autocomplete_fields = ["pilot_boarding_places"]
    model = s127.models.PilotService
    extra = 0


class FullPilotServiceInline(PilotServiceInlineMixin, FeatureTypeInline):
    exclude = ["geometry"]


class SimplePilotServiceInline(
    PilotServiceInlineMixin, nested_admin.NestedStackedInline
):
    fields = ["pilot_boarding_places", "remote_pilot"]
    # TODO : add ShipReportInline below when models has been implemented
    inlines = [FeatureNameInline]


@admin.register(s127.models.Applicability)
class ApplicabilityAdmin(nested_admin.NestedModelAdmin, GISModelAdminWithRasterMarine):
    search_fields = ["id"]
    inlines = [InformationInline, VesselsMeasurementsInline]


class OrganisationContactAreaAdmin(admin.ModelAdmin):
    inlines = [SrvContactInline]
    inlines.extend(FeatureTypeAdmin.inlines)


class SupervisedAreaAdmin(admin.ModelAdmin):
    inlines = []
    inlines.extend(OrganisationContactAreaAdmin.inlines)


class ReportableServiceAreaAdmin(admin.ModelAdmin):
    inlines = []
    inlines.extend(SupervisedAreaAdmin.inlines)


@admin.register(s127.models.PilotageDistrict)
class PilotageDistrictAdmin(GISModelAdminWithRasterMarine, FeatureTypeAdmin):
    search_fields = ["id"]


@admin.register(s127.models.SimplePilotageDistrictProxy)
class SimplePilotageAdmin(
    ModelAdminWithOrderedFormsets, GISModelAdminWithRasterMarine, FeatureTypeAdmin
):
    search_fields = ["id"]
    fieldsets = [
        (
            None,
            {
                "fields": [
                    "geometry",
                    "communication_channel",
                ]
            },
        ),
    ]

    inlines = [SimplePilotServiceInline] + FeatureTypeAdmin.inlines
    fieldsets_and_inlines_order = (FeatureNameInline,)


@admin.register(s127.models.FullPilotageDistrictProxy)
class FullPilotageAdmin(
    ModelAdminWithOrderedFormsets, GISModelAdminWithRasterMarine, FeatureTypeAdmin
):
    search_fields = ["id"]
    inlines = FeatureTypeInlinesMixin.inlines + [FullPilotServiceInline]
    fieldsets_and_inlines_order = (FeatureNameInline,)


# FIXME Add ContactInline
# FIXME Ajouter dans les inlines du simple et full form
@admin.register(s127.models.PilotService)
class PilotServiceAdmin(GISModelAdminWithRasterMarine, FeatureTypeAdmin):
    autocomplete_fields = ["pilotage_district", "pilot_boarding_places"]


# FIXME Add ContactInline
# FIXME Ajouter dans les inlines du simple et full form
@admin.register(s127.models.PilotBoardingPlace)
class PilotBoardingPlaceAdmin(GISModelAdminWithRasterMarine, FeatureTypeAdmin):
    search_fields = ["id"]
