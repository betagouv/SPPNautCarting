from django.contrib import admin
import pytest
from django.contrib.admin.filters import ImproperlyConfigured
from django.contrib.admin.helpers import InlineAdminFormSet
from django.template.response import TemplateResponse

from carting.admin import (
    ModelAdminWithFormsetsIncludingInline,
    ModelAdminWithOrderedFormsets,
)
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


class TestModelAdminWithFormsetsIncludingInline:
    def test_basic(self, rf, admin_user):
        class PilotageDistrictAdmin(ModelAdminWithFormsetsIncludingInline):
            pass

        pilotage_district_admin = PilotageDistrictAdmin(
            PilotageDistrict, admin.AdminSite()
        )
        request = rf.get("")
        request.user = admin_user
        response = pilotage_district_admin.add_view(request)

        assert response.context_data["inline_admin_formsets_by_fieldset_name"] == {}
        assert pilotage_district_admin.get_inlines() == []
        assert pilotage_district_admin.get_fieldsets() == []

    def test_without_inlines(self, rf, admin_user):
        class PilotageDistrictAdmin(ModelAdminWithFormsetsIncludingInline):
            fieldsets_and_inlines_ordered = [
                (None, {"fields": ["communication_channel"]})
            ]

        pilotage_district_admin = PilotageDistrictAdmin(
            PilotageDistrict, admin.AdminSite()
        )
        request = rf.get("")
        request.user = admin_user
        response = pilotage_district_admin.add_view(request)

        assert response.context_data["inline_admin_formsets_by_fieldset_name"] == {
            None: []
        }
        assert pilotage_district_admin.get_inlines() == []
        assert (
            pilotage_district_admin.get_fieldsets()
            == PilotageDistrictAdmin.fieldsets_and_inlines_ordered
        )

    def test_with_inlines(self, rf, admin_user):
        class PilotageDistrictAdmin(ModelAdminWithFormsetsIncludingInline):
            fieldsets_and_inlines_ordered = [(None, {"fields": [FeatureNameInline]})]

        pilotage_district_admin = PilotageDistrictAdmin(
            PilotageDistrict, admin.AdminSite()
        )
        request = rf.get("")
        request.user = admin_user
        response = pilotage_district_admin.add_view(request)

        assert isinstance(
            response.context_data["inline_admin_formsets_by_fieldset_name"][None][0],
            InlineAdminFormSet,
        )
        assert pilotage_district_admin.get_inlines() == [FeatureNameInline]
        assert pilotage_district_admin.get_fieldsets() == [(None, {"fields": []})]

    def test_assert_improperly_configured_is_raised(self, rf, admin_user):
        class PilotageDistrictAdmin(ModelAdminWithFormsetsIncludingInline):
            fieldsets = ["coucou"]
            fieldsets_and_inlines_order = (FeatureNameInline, "fieldset_name", None)

        with pytest.raises(ImproperlyConfigured):
            PilotageDistrictAdmin(
                PilotageDistrict, admin.AdminSite()
            )

        class PilotageDistrictAdmin(ModelAdminWithFormsetsIncludingInline):
            inlines = ["coucou"]
            fieldsets_and_inlines_order = (FeatureNameInline, "fieldset_name", None)

        with pytest.raises(ImproperlyConfigured):
            PilotageDistrictAdmin(
                PilotageDistrict, admin.AdminSite()
            )
    def test_full(self, rf, admin_user):
        class PilotageDistrictAdmin(ModelAdminWithFormsetsIncludingInline):
            fieldsets_and_inlines_ordered = [
                (
                    None,
                    {
                        "fields": [
                            "communication_channel",
                            FeatureNameInline,
                            "geometry",
                        ]
                    },
                ),
                (
                    "un nom de fieldset",
                    {
                        "fields": [
                            FeatureTypePermissionTypeInline,
                            TextContentInline,
                            "communication_channel",
                            FeatureNameInline,
                        ]
                    },
                ),
            ]

        pilotage_district_admin = PilotageDistrictAdmin(
            PilotageDistrict, admin.AdminSite()
        )
        request = rf.get("")
        request.user = admin_user
        response = pilotage_district_admin.add_view(request)

        assert pilotage_district_admin.get_inlines() == [
            FeatureNameInline,
            FeatureTypePermissionTypeInline,
            TextContentInline,
            FeatureNameInline,
        ]
        assert pilotage_district_admin.get_fieldsets() == [
            (
                None,
                {
                    "fields": [
                        "communication_channel",
                        "geometry",
                    ]
                },
            ),
            (
                "un nom de fieldset",
                {
                    "fields": [
                        "communication_channel",
                    ]
                },
            ),
        ]
        assert isinstance(
            response.context_data["inline_admin_formsets_by_fieldset_name"][None][
                0
            ].opts,
            FeatureNameInline,
        )

        for index, inline in enumerate(
            [
                FeatureTypePermissionTypeInline,
                TextContentInline,
                FeatureNameInline,
            ]
        ):
            assert isinstance(
                response.context_data["inline_admin_formsets_by_fieldset_name"][
                    "un nom de fieldset"
                ][index].opts,
                inline,
            )

    def test_template(self):
        class PilotageDistrictAdmin(ModelAdminWithFormsetsIncludingInline):
            pass

        assert (
            PilotageDistrictAdmin.change_form_template
            == "admin/change_form_with_inlines_in_fieldsets.html"
        )


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

