import pytest
from django.contrib.gis.geos import MultiPolygon, Polygon

from s100.models import FeatureName
from s127.models import ContactDetails, PilotageDistrict, PilotService


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


@pytest.mark.parametrize(
    "model_factory,model_name",
    [
        (
            lambda: PilotageDistrict(
                geometry=MultiPolygon([Polygon.from_bbox((0, 0, 0, 0))])
            ),
            "PilotageDistrict",
        ),
        (lambda: PilotService(), "PilotService"),
        (lambda: ContactDetails(), "ContactDetails"),
    ],
)
class TestStrUsingFeatureNames:
    def test_not_saved(self, model_factory, model_name):
        assert str(model_factory()) == f"{model_name} object (None)"

    @pytest.mark.django_db
    def test_without_feature_name(self, model_factory, model_name):
        model = model_factory()
        model.save()
        assert str(model) == f"{model_name} object ({model.id})"

    @pytest.mark.django_db
    def test_with_multiple_feature_names(self, model_factory, model_name):
        model = model_factory()
        model.save()
        model.feature_names.create(name="first", language="fra")
        model.feature_names.create(name="second", language="fra")
        assert str(model) == "first (fra)"

    @pytest.mark.django_db
    def test_uses_the_display_name(self, model_factory, model_name):
        model = model_factory()
        model.save()
        model.feature_names.create(name="first", language="fra")
        model.feature_names.create(
            name="first display", language="fra", display_name=True
        )
        model.feature_names.create(name="second", language="fra")
        assert str(model) == "first display (✓ fra)"
