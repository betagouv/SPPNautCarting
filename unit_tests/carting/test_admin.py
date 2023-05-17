from django.contrib import admin
from django.template.response import TemplateResponse

from carting.admin import ModelAdminWithOrderedFormsets
from s100.admin import FeatureNameInline, TextContentInline
from s127.admin import FeatureTypePermissionTypeInline
from s127.models import PilotageDistrict


def fieldsets_and_inlines_names(response: TemplateResponse):
    return [
        hasattr(fieldset_or_inline, "opts")
        and fieldset_or_inline.opts.verbose_name
        or getattr(fieldset_or_inline, "name")
        for fieldset_or_inline in response.context_data["fieldsets_and_inlines"]
    ]


class TestModelAdminWithOrderedFormsets:
    def test_basic(self, rf, admin_user):
        class PilotageDistrictAdmin(ModelAdminWithOrderedFormsets):
            pass

        pilotage_district_admin = PilotageDistrictAdmin(
            PilotageDistrict, admin.AdminSite()
        )
        request = rf.get("")
        request.user = admin_user
        response = pilotage_district_admin.add_view(request)

        assert fieldsets_and_inlines_names(response) == [None]

    def test_no_order_respects_fieldesets_order(self, rf, admin_user):
        class PilotageDistrictAdmin(ModelAdminWithOrderedFormsets):
            fieldsets = [
                (None, {"fields": ["geometry"]}),
                ("fieldset_name", {"fields": ["communication_channel"]}),
            ]

        pilotage_district_admin = PilotageDistrictAdmin(
            PilotageDistrict, admin.AdminSite()
        )
        request = rf.get("")
        request.user = admin_user
        response = pilotage_district_admin.add_view(request)

        assert fieldsets_and_inlines_names(response) == [None, "fieldset_name"]

    def test_all_fieldsets_explicitly_ordered(self, rf, admin_user):
        class PilotageDistrictAdmin(ModelAdminWithOrderedFormsets):
            fieldsets = [
                (None, {"fields": ["geometry"]}),
                ("fieldset_name", {"fields": ["communication_channel"]}),
            ]
            fieldsets_and_inlines_order = ("fieldset_name", None)

        pilotage_district_admin = PilotageDistrictAdmin(
            PilotageDistrict, admin.AdminSite()
        )
        request = rf.get("")
        request.user = admin_user
        response = pilotage_district_admin.add_view(request)

        assert fieldsets_and_inlines_names(response) == ["fieldset_name", None]

    def test_some_fieldsets_explicitly_ordered(self, rf, admin_user):
        class PilotageDistrictAdmin(ModelAdminWithOrderedFormsets):
            fieldsets = [
                (None, {"fields": ["geometry"]}),
                ("fieldset_name", {"fields": ["communication_channel"]}),
            ]
            fieldsets_and_inlines_order = ("fieldset_name",)

        pilotage_district_admin = PilotageDistrictAdmin(
            PilotageDistrict, admin.AdminSite()
        )
        request = rf.get("")
        request.user = admin_user
        response = pilotage_district_admin.add_view(request)

        assert fieldsets_and_inlines_names(response) == ["fieldset_name", None]

    def test_no_order_respects_inlines_order(self, rf, admin_user):
        class PilotageDistrictAdmin(ModelAdminWithOrderedFormsets):
            inlines = [
                FeatureNameInline,
                FeatureTypePermissionTypeInline,
                TextContentInline,
            ]

        pilotage_district_admin = PilotageDistrictAdmin(
            PilotageDistrict, admin.AdminSite()
        )
        request = rf.get("")
        request.user = admin_user
        response = pilotage_district_admin.add_view(request)
        assert fieldsets_and_inlines_names(response) == [
            None,
            "feature name",
            "permission type",
            "text content",
        ]

    def test_all_inlines_explicitly_ordered(self, rf, admin_user):
        class PilotageDistrictAdmin(ModelAdminWithOrderedFormsets):
            inlines = [
                FeatureNameInline,
                FeatureTypePermissionTypeInline,
                TextContentInline,
            ]
            fieldsets_and_inlines_order = (
                FeatureTypePermissionTypeInline,
                TextContentInline,
                FeatureNameInline,
            )

        pilotage_district_admin = PilotageDistrictAdmin(
            PilotageDistrict, admin.AdminSite()
        )
        request = rf.get("")
        request.user = admin_user
        response = pilotage_district_admin.add_view(request)
        assert fieldsets_and_inlines_names(response) == [
            "permission type",
            "text content",
            "feature name",
            None,
        ]

    def test_some_inlines_explicitly_ordered(self, rf, admin_user):
        class PilotageDistrictAdmin(ModelAdminWithOrderedFormsets):
            inlines = [
                FeatureNameInline,
                FeatureTypePermissionTypeInline,
                TextContentInline,
            ]
            fieldsets_and_inlines_order = (FeatureNameInline,)

        pilotage_district_admin = PilotageDistrictAdmin(
            PilotageDistrict, admin.AdminSite()
        )
        request = rf.get("")
        request.user = admin_user
        response = pilotage_district_admin.add_view(request)
        assert fieldsets_and_inlines_names(response) == [
            "feature name",
            None,
            "permission type",
            "text content",
        ]

    def test_mix_fieldsets_and_inlines_explicitly_ordered(self, rf, admin_user):
        class PilotageDistrictAdmin(ModelAdminWithOrderedFormsets):
            fieldsets = [
                (None, {"fields": ["geometry"]}),
                ("fieldset_name", {"fields": ["communication_channel"]}),
            ]
            inlines = [
                FeatureNameInline,
                FeatureTypePermissionTypeInline,
                TextContentInline,
            ]
            fieldsets_and_inlines_order = (FeatureNameInline, "fieldset_name", None)

        pilotage_district_admin = PilotageDistrictAdmin(
            PilotageDistrict, admin.AdminSite()
        )
        request = rf.get("")
        request.user = admin_user
        response = pilotage_district_admin.add_view(request)
        assert fieldsets_and_inlines_names(response) == [
            "feature name",
            "fieldset_name",
            None,
            "permission type",
            "text content",
        ]
