import nested_admin
from django.contrib import admin

import s127
from carting.admin import GISModelAdminWithRasterMarine, ModelAdminWithOrderedFormsets
from s100.admin import FeatureNameInline, InformationInline, TextContentInline


class VesselsMeasurementsInline(nested_admin.NestedStackedInline):
    verbose_name_plural = "Vessel measurements"
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

    def get_fieldsets(self, request, obj=None):
        """
        Hook for specifying fieldsets.
        """
        # if self.fieldsets:
        #     return self.fieldsets
        return [
            (
                "Language",
                {"fields": ["language"]},
            ),
            (
                "Main Radiocommunication",
                {
                    "fields": [
                        x for x in self.get_fields(request, obj) if x != "language"
                    ]
                },
            ),
        ]

    inlines = [TelecommunicationsInline, ContactAddressInline, InformationInline]


class PilotBoardingPlaceInline(nested_admin.NestedStackedInline):
    inlines = [FeatureNameInline]
    model = s127.models.PilotBoardingPlace
    extra = 0


class SrvContactInline(nested_admin.NestedGenericTabularInline):
    ct_field = "contactable_content_type"
    ct_fk_field = "contactable_object_id"
    model = s127.models.SrvContact
    verbose_name = "Contact Detail"

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


class AccumulatedInlines:
    def get_inlines(self, *args, **kwargs):
        accumulated_inlines = []
        for ancestor_class in type(self).mro():
            accumulated_inlines.extend(getattr(ancestor_class, "inlines", []))
        return list(dict.fromkeys(accumulated_inlines).keys())


class FeatureTypeInlinesMixin(AccumulatedInlines):
    inlines = [
        FeatureNameInline,
        FeatureTypePermissionTypeInline,
        TextContentInline,
    ]


class FeatureTypeAdmin(FeatureTypeInlinesMixin, nested_admin.NestedModelAdmin):
    pass


class FeatureTypeInline(FeatureTypeInlinesMixin, nested_admin.NestedStackedInline):
    pass


class ContactableAreaAdmin(FeatureTypeAdmin):
    inlines = [SrvContactInline]


class SupervisedAreaAdmin(ContactableAreaAdmin):
    pass


class ReportableServiceAreaAdmin(SupervisedAreaAdmin):
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


class NoticeTimeInline(nested_admin.NestedStackedInline):
    model = s127.models.NoticeTime
    extra = 0
    max_num = 2


@admin.register(s127.models.Applicability)
class ApplicabilityAdmin(
    ModelAdminWithOrderedFormsets,
    nested_admin.NestedModelAdmin,
    GISModelAdminWithRasterMarine,
):
    search_fields = ["id"]
    inlines = [InformationInline, VesselsMeasurementsInline]
    fieldsets_and_inlines_order = (
        None,
        VesselsMeasurementsInline,
    )

    fieldsets = [
        (
            None,
            {
                "fields": [
                    "logical_connectives",
                ]
            },
        ),
        (
            "Ballast & Performances",
            {
                "fields": [
                    "in_ballast",
                    "thickness_of_ice_capability",
                    "vessel_performance",
                ]
            },
        ),
        (
            "Cargo category",
            {
                "fields": [
                    "category_of_cargo",
                    "category_of_dangerous_or_hazardous_cargo",
                ]
            },
        ),
        (
            "Vessels category",
            {
                "fields": [
                    "category_of_vessel",
                    "category_of_vessel_registry",
                ]
            },
        ),
    ]

    # fieldsets = [
    #     ("Geometry", {"fields": ["geometry"]}),
    #     ("Communication channel", {"fields": ["communication_channel"]}),
    # ]


@admin.register(s127.models.PilotageDistrict)
class PilotageDistrictAdmin(
    ModelAdminWithOrderedFormsets, GISModelAdminWithRasterMarine, FeatureTypeAdmin
):
    search_fields = ["id"]

    fieldsets_and_inlines_order = (
        FeatureNameInline,
        "Geometry",
        "Communication channel",
    )

    fieldsets = [
        ("Geometry", {"fields": ["geometry"]}),
        ("Communication channel", {"fields": ["communication_channel"]}),
    ]


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

    inlines = [SimplePilotServiceInline]
    fieldsets_and_inlines_order = (FeatureNameInline,)


@admin.register(s127.models.FullPilotageDistrictProxy)
class FullPilotageAdmin(
    ModelAdminWithOrderedFormsets, GISModelAdminWithRasterMarine, FeatureTypeAdmin
):
    search_fields = ["id"]
    inlines = [FullPilotServiceInline]
    fieldsets_and_inlines_order = (
        FeatureNameInline,
        "communication channel",
        "geometry",
        FullPilotServiceInline,
    )
    fieldsets = [
        ("communication channel", {"fields": ["communication_channel"]}),
        ("geometry", {"fields": ["geometry"]}),
    ]


# FIXME : Les géométries à part c'est cool parce que la carte attire l'attention


@admin.register(s127.models.PilotService)
class PilotServiceAdmin(GISModelAdminWithRasterMarine, ReportableServiceAreaAdmin):
    autocomplete_fields = ["pilotage_district", "pilot_boarding_places"]


@admin.register(s127.models.PilotBoardingPlace)
class PilotBoardingPlaceAdmin(
    ModelAdminWithOrderedFormsets, GISModelAdminWithRasterMarine, ContactableAreaAdmin
):
    search_fields = ["id"]
    fieldsets_and_inlines_order = (
        FeatureNameInline,
        "Geometry",
        "Communication",
        "Details",
    )

    fieldsets = (
        (
            "Communication",
            {
                "fields": (
                    "communication_channel",
                    "call_sign",
                ),
            },
        ),
        (
            "Details",
            {
                "fields": (
                    "category_of_pilot_boarding_place",
                    "category_of_preference",
                    "category_of_vessel",
                    "destination",
                    "pilot_movement",
                    "pilot_vessel",
                    "status",
                ),
            },
        ),
        ("Geometry", {"fields": ["geometry"]}),
    )


@admin.register(s127.models.FullPilotServiceProxy)
class FullPilotServiceAdmin(
    ModelAdminWithOrderedFormsets,
    GISModelAdminWithRasterMarine,
    ReportableServiceAreaAdmin,
):
    autocomplete_fields = ["pilotage_district", "pilot_boarding_places"]
    inlines = [NoticeTimeInline]

    fieldsets_and_inlines_order = (
        FeatureNameInline,
        "Geometry",
        "Pilotage district",
        SrvContactInline,
        FeatureTypePermissionTypeInline,
        "Pilot boarding places",
        NoticeTimeInline,
    )

    fieldsets = [
        ("Geometry", {"fields": ["geometry"]}),
        ("Pilotage district", {"fields": ["pilotage_district"]}),
        ("Pilot boarding places", {"fields": ["pilot_boarding_places"]}),
        (
            "Pilot details",
            {
                "fields": [
                    "category_of_pilot",
                    "remote_pilot",
                    "pilot_qualification",
                    "pilot_request",
                ]
            },
        ),
    ]
