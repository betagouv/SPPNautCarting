import nested_admin
from django.contrib import admin

import s127.models
from carting.admin import (GISModelAdminWithRasterMarine,
                           ModelAdminWithOrderedFormsets)
from s100.admin import FeatureNameInline, InformationInline, TextContentInline

# region Inlines


class VesselsMeasurementsInline(nested_admin.NestedStackedInline):
    verbose_name_plural = "Vessel measurements"
    model = s127.models.VesselsMeasurements
    extra = 0
    is_sortable = False


class ContactAddressInline(nested_admin.NestedStackedInline):
    model = s127.models.ContactAddress
    extra = 0
    is_sortable = False


class TelecommunicationsInline(nested_admin.NestedStackedInline):
    model = s127.models.Telecommunications
    extra = 1
    is_sortable = False


class RadiocommunicationsInline(nested_admin.NestedStackedInline):
    model = s127.models.Radiocommunications
    extra = 0
    is_sortable = False


class NoticeTimeInline(nested_admin.NestedStackedInline):
    model = s127.models.NoticeTime
    extra = 1
    max_num = 1


class PilotServicePilotBoardingPlaceInline(nested_admin.NestedTabularInline):
    model = s127.models.PilotService.pilot_boarding_places.through
    autocomplete_fields = ["pilot_boarding_place"]
    verbose_name = "Pilot boarding place"

    def get_extra(self, request, obj=None, **kwargs):
        if not obj:
            return 1
        if obj.pilot_boarding_places.count():
            return 0
        return 1


class SrvContactInline(nested_admin.NestedGenericTabularInline):
    ct_field = "contactable_content_type"
    ct_fk_field = "contactable_object_id"
    model = s127.models.SrvContact
    verbose_name = "Contact Detail"

    min_num = 0
    extra = 0
    autocomplete_fields = ["contact_details"]
    is_sortable = False


class FeatureTypePermissionTypeInline(nested_admin.NestedGenericTabularInline):
    ct_field = "feature_content_type"
    ct_fk_field = "feature_object_id"
    model = s127.models.PermissionType

    min_num = 0
    extra = 0
    autocomplete_fields = ["applicability"]
    is_sortable = False


# endregion Inlines


class AccumulatedInlines:
    def get_inlines(self, *args, **kwargs):
        accumulated_inlines = []
        for ancestor_class in type(self).mro():
            accumulated_inlines.extend(getattr(ancestor_class, "inlines", []))
        return list(dict.fromkeys(accumulated_inlines).keys())


# region InformationTypeAdmins


class InformationTypeAdmin(
    AccumulatedInlines, ModelAdminWithOrderedFormsets, nested_admin.NestedModelAdmin
):
    inlines = [InformationInline]


@admin.register(s127.models.ContactDetails)
class ContactDetailsAdmin(InformationTypeAdmin):
    search_fields = ["id", "feature_names__name"]

    def get_fieldsets(self, request, obj=None):
        return [
            (
                "Language",
                {"fields": ["language"]},
            ),
            (
                "Main Radiocommunication",
                {
                    "fields": [
                        # FIXME: Write a generic concept to "dump" the fields
                        # that were not mentioned in other fieldsets
                        x
                        for x in self.get_fields(request, obj)
                        if x != "language"
                    ]
                },
            ),
        ]

    inlines = [
        FeatureNameInline,
        RadiocommunicationsInline,
        TelecommunicationsInline,
        ContactAddressInline,
    ]
    fieldsets_and_inlines_order = (FeatureNameInline,)


@admin.register(s127.models.Applicability)
class ApplicabilityAdmin(InformationTypeAdmin):
    search_fields = ["id"]
    inlines = [VesselsMeasurementsInline]
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


# endregion InformationTypeAdmins

# region FeatureTypeAdmins


class FeatureTypeAdmin(
    AccumulatedInlines,
    ModelAdminWithOrderedFormsets,
    GISModelAdminWithRasterMarine,
    nested_admin.NestedModelAdmin,
):
    inlines = [
        FeatureNameInline,
        FeatureTypePermissionTypeInline,
        TextContentInline,
    ]


class ContactableAreaAdmin(FeatureTypeAdmin):
    inlines = [SrvContactInline]


class SupervisedAreaAdmin(ContactableAreaAdmin):
    pass


class ReportableServiceAreaAdmin(SupervisedAreaAdmin):
    pass


@admin.register(s127.models.PilotageDistrict)
class PilotageDistrictAdmin(FeatureTypeAdmin):
    search_fields = ["id", "feature_names__name"]
    list_display = (
        "__str__",
        "pilot_services",
        "pilot_boarding_places",
    )

    fieldsets_and_inlines_order = (
        FeatureNameInline,
        "Geometry",
        "Communication channel",
    )

    fieldsets = [
        ("Geometry", {"fields": ["geometry"]}),
        ("Communication channel", {"fields": ["communication_channel"]}),
    ]

    @admin.display(description="Pilot Services")
    def pilot_services(self, obj):
        pilot_services = obj.pilot_services.all()
        return ", ".join(str(pilot_service) for pilot_service in pilot_services)

    @admin.display(description="Pilot Boarding Places")
    def pilot_boarding_places(self, obj):
        pilot_boarding_places = s127.models.PilotBoardingPlace.objects.filter(
            pilotservice__pilotage_district=obj
        ).distinct()
        return ", ".join(
            str(pilot_boarding_place) for pilot_boarding_place in pilot_boarding_places
        )


@admin.register(s127.models.PilotBoardingPlace)
class PilotBoardingPlaceAdmin(ContactableAreaAdmin):
    search_fields = [
        "id",
        "feature_names__name",
        "pilotage_district__feature_names__name",
    ]
    list_display = ("__str__", "pilot_services", "pilotage_district")
    list_filter = ("pilotservice__pilotage_district",)

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

    @admin.display(description="Pilot Services")
    def pilot_services(self, obj):
        pilot_services = obj.pilotservice_set.all()
        return ", ".join(str(pilot_service) for pilot_service in pilot_services)

    @admin.display(description="Pilotage District")
    def pilotage_districts(self, obj):
        pilot_service = obj.pilotservice_set.first()
        if not pilot_service:
            return ""
        return str(pilot_service.pilotage_district)


@admin.register(s127.models.PilotService)
class PilotServiceAdmin(ReportableServiceAreaAdmin):
    autocomplete_fields = ["pilotage_district", "pilot_boarding_places"]
    search_fields = [
        "id",
        "feature_names__name",
        "pilotage_district__feature_names__name",
    ]

    list_display = (
        "__str__",
        "pilotage_district",
        "pilot_boarding_places_display",
    )
    list_filter = ("pilotage_district",)

    @admin.display(description="Pilot Boarding Places")
    def pilot_boarding_places_display(self, obj):
        pilot_boarding_places = obj.pilot_boarding_places.all()
        return ", ".join(
            str(pilot_boarding_place) for pilot_boarding_place in pilot_boarding_places
        )


@admin.register(s127.models.FullPilotServiceProxy)
class FullPilotServiceAdmin(PilotServiceAdmin):
    autocomplete_fields = ["pilotage_district"]
    inlines = [NoticeTimeInline, PilotServicePilotBoardingPlaceInline]

    fieldsets_and_inlines_order = (
        FeatureNameInline,
        "Pilotage district",
        PilotServicePilotBoardingPlaceInline,
        SrvContactInline,
        FeatureTypePermissionTypeInline,
        NoticeTimeInline,
        "Geometry",
    )

    fieldsets = [
        ("Geometry", {"fields": ["geometry"], "classes": ["collapse"]}),
        ("Pilotage district", {"fields": ["pilotage_district"]}),
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


# endregion FeatureTypeAdmins
