import pytest
from django.contrib.gis.geos import MultiPolygon, Polygon

from s100.models import FeatureName
from s127.models import PilotageDistrict


class TestFeatureNameStr:
    def test_empty(self):
        assert str(FeatureName()) == " ()"

    def test_basic(self):
        assert str(FeatureName(language="fra", name="yolo")) == "yolo (fra)"

    def test_with_display(self):
        assert (
            str(FeatureName(language="fra", name="yolo", display_name=True))
            == "yolo (✓ fra)"
        )


class TestFeatureTypeStr:
    @pytest.mark.django_db
    def test_not_saved(self):
        assert (
            str(
                PilotageDistrict(
                    geometry=MultiPolygon([Polygon.from_bbox((0, 0, 0, 0))])
                )
            )
            == "PilotageDistrict object (None)"
        )

    @pytest.mark.django_db
    def test_without_feature_name(self):
        pilotage_district = PilotageDistrict(
            geometry=MultiPolygon([Polygon.from_bbox((0, 0, 0, 0))])
        )
        pilotage_district.save()
        assert (
            str(pilotage_district)
            == f"PilotageDistrict object ({pilotage_district.id})"
        )

    @pytest.mark.django_db
    def test_with_multiple_feature_names(self):
        pilotage_district = PilotageDistrict(
            geometry=MultiPolygon([Polygon.from_bbox((0, 0, 0, 0))]),
        )
        pilotage_district.save()
        pilotage_district.feature_names.create(name="first", language="fra")
        pilotage_district.feature_names.create(name="second", language="fra")
        assert str(pilotage_district) == "first (fra)"

    @pytest.mark.django_db
    def test_uses_the_display_name(self):
        pilotage_district = PilotageDistrict(
            geometry=MultiPolygon([Polygon.from_bbox((0, 0, 0, 0))]),
        )
        pilotage_district.save()
        pilotage_district.feature_names.create(name="first", language="fra")
        pilotage_district.feature_names.create(
            name="first display", language="fra", display_name=True
        )
        pilotage_district.feature_names.create(name="second", language="fra")
        assert str(pilotage_district) == f"first display (✓ fra)"
