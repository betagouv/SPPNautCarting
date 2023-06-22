import nested_admin
from django.contrib import admin

import s127.models
from carting.admin import (
    GISModelAdminWithRasterMarine,
    ModelAdminWithFormsetsIncludingInline,
)
from s100.admin import FeatureNameInline, InformationInline, TextContentInline

# region Inlines


class VesselsMeasurementsInline(nested_admin.NestedStackedInline):
    verbose_name_plural = "Vessel measurements"
    model = s127.models.VesselsMeasurements
    extra = 1
    is_sortable = False


class ContactAddressInline(nested_admin.NestedStackedInline):
    # FIXME : display one by default, with OneExtraWhenEmptyMixin that works
    model = s127.models.ContactAddress
    extra = 0
    is_sortable = False


class TelecommunicationsInline(nested_admin.NestedStackedInline):
    model = s127.models.Telecommunications
    extra = 1
    is_sortable = False


class RadiocommunicationsInline(nested_admin.NestedStackedInline):
    # FIXME : display one by default, with OneExtraWhenEmptyMixin that works
    model = s127.models.Radiocommunications
    extra = 0
    is_sortable = False


class NoticeTimeInline(nested_admin.NestedStackedInline):
    model = s127.models.NoticeTime
    extra = 1
    max_num = 1


class PilotServicePilotBoardingPlaceInline(nested_admin.NestedTabularInline):
    model = s127.models.PilotService.pilot_boarding_places.through
    autocomplete_fields = ["pilotboardingplace"]
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
    # FIXME : display one by default, with OneExtraWhenEmptyMixin that works
    ct_field = "feature_content_type"
    ct_fk_field = "feature_object_id"
    model = s127.models.PermissionType

    min_num = 0
    extra = 0
    autocomplete_fields = ["applicability"]
    is_sortable = False


# endregion Inlines


# region InformationTypeAdmins


class InformationTypeAdmin(nested_admin.NestedModelAdmin):
    inlines = [InformationInline]


@admin.register(s127.models.ContactDetails)
class ContactDetailsAdmin(ModelAdminWithFormsetsIncludingInline, InformationTypeAdmin):
    search_fields = ["id", "feature_names__name"]

    fieldsets_and_inlines_ordered = [
        ("Feature names", {"fields": [FeatureNameInline]}),
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
                    x.name
                    for x in s127.models.ContactDetails._meta.get_fields()
                    if x.name
                    not in [
                        "id",
                        "language",
                        "feature_names",
                        "information",
                        "srvcontact",
                        "telecommunications",
                        "contact_addresses",
                        "radiocommunications",
                    ]
                ]
            },
        ),
        (
            "Telecommunications",
            {
                "fields": [TelecommunicationsInline],
            },
        ),
        (
            "Radiocommunications",
            {
                "fields": [RadiocommunicationsInline],
                "classes": ["collapse"],
            },
        ),
        (
            "Contact addresses",
            {
                "fields": [ContactAddressInline],
                "classes": ["collapse"],
            },
        ),
        (
            "Informations",
            {
                "fields": [InformationInline],
                "classes": ["collapse"],
            },
        ),
    ]


@admin.register(s127.models.Applicability)
class ApplicabilityAdmin(
    ModelAdminWithFormsetsIncludingInline,
    InformationTypeAdmin,
):
    search_fields = ["id"]

    fieldsets_and_inlines_ordered = [
        (
            "Vessels Measurements",
            {
                "fields": ["logical_connectives", VesselsMeasurementsInline],
            },
        ),
        (
            "Cargo category",
            {
                "fields": [
                    "category_of_cargo",
                ]
            },
        ),
        (
            "Dangerous or hazardous detail",
            {
                "fields": [
                    "category_of_dangerous_or_hazardous_cargo",
                ],
                "classes": ["collapse"],
            },
        ),
        (
            "Ballast & Performances",
            {
                "fields": [
                    "in_ballast",
                    "thickness_of_ice_capability",
                    "vessel_performance",
                ],
                "classes": ["collapse"],
            },
        ),
        (
            "Vessels category",
            {
                "fields": [
                    "category_of_vessel",
                    "category_of_vessel_registry",
                ],
                "classes": ["collapse"],
            },
        ),
        (
            "Informations",
            {"fields": [InformationInline], "classes": ["collapse"]},
        ),
    ]


# endregion InformationTypeAdmins

# region FeatureTypeAdmins


class FeatureTypeAdmin(GISModelAdminWithRasterMarine, nested_admin.NestedModelAdmin):
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
class PilotageDistrictAdmin(ModelAdminWithFormsetsIncludingInline, FeatureTypeAdmin):
    search_fields = ["id", "feature_names__name"]
    list_display = (
        "__str__",
        "pilot_services",
        "pilot_boarding_places",
    )

    fieldsets_and_inlines_ordered = [
        ("Feature names", {"fields": [FeatureNameInline]}),
        ("Geometry", {"fields": ["geometry"]}),
        ("Permission types", {"fields": [FeatureTypePermissionTypeInline]}),
        ("Text contents", {"fields": [TextContentInline], "classes": ["collapse"]}),
        (
            "Communication channel",
            {"fields": ["communication_channel"], "classes": ["collapse"]},
        ),
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
class PilotBoardingPlaceAdmin(
    ModelAdminWithFormsetsIncludingInline, ContactableAreaAdmin
):
    search_fields = [
        "id",
        "feature_names__name",
        "pilotservice__pilotage_district__feature_names__name",
    ]
    list_display = ("__str__", "pilot_services", "pilotage_districts")
    list_filter = ("pilotservice__pilotage_district",)

    fieldsets_and_inlines_ordered = (
        ("Feature names", {"fields": [FeatureNameInline]}),
        ("Geometry", {"fields": ["geometry"]}),
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
        (
            "Communication",
            {
                "fields": (
                    "communication_channel",
                    "call_sign",
                ),
                "classes": ["collapse"],
            },
        ),
        ("Contact details", {"fields": [SrvContactInline], "classes": ["collapse"]}),
        (
            "Permission types",
            {"fields": [FeatureTypePermissionTypeInline], "classes": ["collapse"]},
        ),
        ("Text contents", {"fields": [TextContentInline], "classes": ["collapse"]}),
    )

    fieldsets = ()

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
        "pilot_boarding_places",
    )
    list_filter = ("pilotage_district",)

    @admin.display(description="Pilot Boarding Places")
    def pilot_boarding_places(obj):
        pilot_boarding_places = obj.pilot_boarding_places.all()
        return ", ".join(
            str(pilot_boarding_place) for pilot_boarding_place in pilot_boarding_places
        )


@admin.register(s127.models.FullPilotServiceProxy)
class FullPilotServiceAdmin(
    ModelAdminWithFormsetsIncludingInline,
    PilotServiceAdmin,
):
    autocomplete_fields = ["pilotage_district"]

    list_display = (
        "__str__",
        "pilotage_district",
        "pilot_boarding_places",
    )
    list_filter = ("pilotage_district",)

    fieldsets_and_inlines_ordered = [
        (
            "Feature names",
            {
                "fields": [
                    FeatureNameInline,
                ]
            },
        ),
        ("Pilotage districts", {"fields": ["pilotage_district"]}),
        (
            "Pilot Boarding Places",
            {"fields": [PilotServicePilotBoardingPlaceInline]},
        ),
        ("Contact Details", {"fields": [SrvContactInline]}),
        ("Permission type", {"fields": [FeatureTypePermissionTypeInline]}),
        ("Notice times", {"fields": [NoticeTimeInline], "classes": ["collapse"]}),
        (
            "Remote pilot",
            {
                "fields": [
                    "remote_pilot",
                ]
            },
        ),
        (
            "Pilot details",
            {
                "fields": [
                    "category_of_pilot",
                    "pilot_qualification",
                    "pilot_request",
                ],
                "classes": ["collapse"],
            },
        ),
        ("Text content", {"fields": [TextContentInline], "classes": ["collapse"]}),
        ("Geometry", {"fields": ["geometry"], "classes": ["collapse"]}),
    ]


# endregion FeatureTypeAdmins
