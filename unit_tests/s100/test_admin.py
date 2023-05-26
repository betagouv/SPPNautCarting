import pytest
from django.contrib import admin
from django.contrib.gis.geos import MultiPolygon, Polygon

from s100.admin import FeatureNameInline
from s127.models import PilotageDistrict


def test_no_object():
    f = FeatureNameInline(None, admin.AdminSite())
    assert f.get_extra(None, obj=None) == 1


@pytest.mark.django_db
def test_object_with_zero_feature_names():
    f = FeatureNameInline(None, admin.AdminSite())
    assert f.get_extra(None, obj=PilotageDistrict()) == 1


@pytest.mark.django_db
def test_object_with_feature_names():
    p = PilotageDistrict.objects.create(
        geometry=MultiPolygon([Polygon.from_bbox((0, 0, 0, 0))])
    )
    p.feature_names.create()
    f = FeatureNameInline(None, admin.AdminSite())
    assert f.get_extra(None, obj=p) == 0
