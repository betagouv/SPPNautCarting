from decimal import Decimal

import pytest
from django.contrib.gis.geos import (
    GeometryCollection,
    LinearRing,
    LineString,
    Point,
    Polygon,
)
from django.core.exceptions import ValidationError

from s127.models import Applicability, PilotBoardingPlace, VesselsMeasurements
from s127.models.shared import CategoryOfVessel


class TestVesselsMeasurementsStr:
    def test_empty(self):
        assert str(VesselsMeasurements()) == "VesselsMeasurements object (None)"

    @pytest.mark.django_db
    def test_basic(self):
        applicability = Applicability()
        applicability.save()
        vessels_measurements = VesselsMeasurements(
            applicability=applicability,
            vessels_characteristics=VesselsMeasurements.VesselsCharacteristics.LENGTH_OVERALL,
            comparison_operator=VesselsMeasurements.ComparisonOperator.GREATER_THAN,
            vessels_characteristics_value=Decimal("1.1"),
            vessels_characteristics_unit=VesselsMeasurements.VesselsCharacteristicsUnit.METRE,
        )
        vessels_measurements.save()
        assert str(vessels_measurements) == f"Length Overall > 1.1 Metre"


class TestApplicabilityStr:
    def test_empty(self):
        assert str(Applicability()) == "Applicability object (None)"

    @pytest.mark.django_db
    def test_empty_saved(self):
        applicability = Applicability()
        applicability.save()
        assert str(applicability) == f"Applicability object ({applicability.pk})"

    @pytest.mark.django_db
    def test_with_in_ballast_true(self):
        applicability = Applicability(in_ballast=True)
        applicability.save()
        assert str(applicability) == "In ballast"

    @pytest.mark.django_db
    def test_with_in_ballast_false(self):
        applicability = Applicability(in_ballast=False)
        applicability.save()
        assert str(applicability) == "Not in ballast"

    @pytest.mark.django_db
    def test_with_category_of_cargo(self):
        applicability = Applicability(
            category_of_cargo=[Applicability.CategoryOfCargo.LIQUID]
        )
        applicability.save()
        assert str(applicability) == "Liquid"

    @pytest.mark.django_db
    def test_with_multiple_category_of_cargo(self):
        applicability = Applicability(
            category_of_cargo=[
                Applicability.CategoryOfCargo.LIQUID,
                Applicability.CategoryOfCargo.LIVESTOCK,
                Applicability.CategoryOfCargo.HEAVY_LIFT,
            ]
        )
        applicability.save()
        assert str(applicability) == "Liquid or Livestock or Heavy Lift"

    @pytest.mark.django_db
    def test_with_dangerous_or_hazardous_cargo(self):
        "FIXME est-ce qu'on veut tester le non multiple ?"

    @pytest.mark.django_db
    def test_with_multiple_dangerous_or_hazardous_cargo(self):
        applicability = Applicability(
            category_of_dangerous_or_hazardous_cargo=[
                Applicability.CategoryOfDangerousOrHazardousCargo.IMDG_CODE_CLASS_1_DIV_1_1,
                Applicability.CategoryOfDangerousOrHazardousCargo.HARMFUL_SUBSTANCES_IN_PACKAGED_FORM,
                Applicability.CategoryOfDangerousOrHazardousCargo.IMDG_CODE_CLASS_3,
            ]
        )
        applicability.save()
        assert (
            str(applicability)
            == "Imdg Code Class 1 Div 1 1 or Harmful Substances In Packaged Form or Imdg Code Class 3"
        )

    @pytest.mark.django_db
    def test_with_category_of_vessel(self):
        applicability = Applicability(category_of_vessel=CategoryOfVessel.TUG_AND_TOW)
        applicability.save()
        assert str(applicability) == "Tug And Tow"

    @pytest.mark.django_db
    def test_with_category_of_vessel_registry(self):
        applicability = Applicability(
            category_of_vessel_registry=Applicability.CategoryOfVesselRegistry.DOMESTIC
        )
        applicability.save()
        assert str(applicability) == "Domestic"

    @pytest.mark.django_db
    def test_with_thickness_of_ice_capability(self):
        applicability = Applicability(thickness_of_ice_capability=1)
        applicability.save()
        assert str(applicability) == "Thickness of ice capability: 1"

    @pytest.mark.django_db
    def test_with_vessel_performance(self):
        applicability = Applicability(vessel_performance="Cool boat")
        applicability.save()
        assert str(applicability) == "Cool boat"

    @pytest.mark.django_db
    def test_with_vessel_performance_greather_than_25_char(self):
        applicability = Applicability(
            vessel_performance="Your boat should be the best of the best"
        )
        applicability.save()
        assert str(applicability) == "Your boat should be the …"

    @pytest.mark.django_db
    def test_with_vessels_measurements(self):
        applicability = Applicability()
        applicability.save()
        vessels_measurements = VesselsMeasurements(
            applicability=applicability,
            vessels_characteristics=VesselsMeasurements.VesselsCharacteristics.LENGTH_OVERALL,
            comparison_operator=VesselsMeasurements.ComparisonOperator.GREATER_THAN,
            vessels_characteristics_value=Decimal("1.1"),
            vessels_characteristics_unit=VesselsMeasurements.VesselsCharacteristicsUnit.METRE,
        )
        vessels_measurements.save()
        assert str(applicability) == f"Length Overall > 1.1 Metre"

    @pytest.mark.django_db
    @pytest.mark.parametrize(
        "logical_connectives,logical_operator",
        [
            (Applicability.LogicalConnectives.LOGICAL_DISJUNCTION, "OR"),
            (Applicability.LogicalConnectives.LOGICAL_CONJUNCTION, "AND"),
            (None, "-"),
        ],
    )
    def test_with_multiple_vessels_measurements(
        self, logical_connectives, logical_operator
    ):
        applicability = Applicability.objects.create(
            logical_connectives=logical_connectives
        )
        VesselsMeasurements.objects.create(
            applicability=applicability,
            vessels_characteristics=VesselsMeasurements.VesselsCharacteristics.LENGTH_OVERALL,
            comparison_operator=VesselsMeasurements.ComparisonOperator.GREATER_THAN,
            vessels_characteristics_value=Decimal("1.1"),
            vessels_characteristics_unit=VesselsMeasurements.VesselsCharacteristicsUnit.METRE,
        )
        VesselsMeasurements.objects.create(
            applicability=applicability,
            vessels_characteristics=VesselsMeasurements.VesselsCharacteristics.LENGTH_OVERALL,
            comparison_operator=VesselsMeasurements.ComparisonOperator.GREATER_THAN,
            vessels_characteristics_value=Decimal("1.2"),
            vessels_characteristics_unit=VesselsMeasurements.VesselsCharacteristicsUnit.METRE,
        )

        assert (
            str(applicability)
            == f"Length Overall > 1.1 Metre {logical_operator} Length Overall > 1.2 Metre"
        )

    @pytest.mark.django_db
    @pytest.mark.parametrize(
        "logical_connectives,logical_operator",
        [
            (Applicability.LogicalConnectives.LOGICAL_DISJUNCTION, "OR"),
            (Applicability.LogicalConnectives.LOGICAL_CONJUNCTION, "AND"),
            (None, "-"),
        ],
    )
    def test_full(self, logical_connectives, logical_operator):
        applicability = Applicability(
            in_ballast=True,
            category_of_cargo=[
                Applicability.CategoryOfCargo.LIQUID,
                Applicability.CategoryOfCargo.LIVESTOCK,
                Applicability.CategoryOfCargo.HEAVY_LIFT,
            ],
            category_of_dangerous_or_hazardous_cargo=[
                Applicability.CategoryOfDangerousOrHazardousCargo.IMDG_CODE_CLASS_1_DIV_1_1,
                Applicability.CategoryOfDangerousOrHazardousCargo.HARMFUL_SUBSTANCES_IN_PACKAGED_FORM,
                Applicability.CategoryOfDangerousOrHazardousCargo.IMDG_CODE_CLASS_3,
            ],
            category_of_vessel=CategoryOfVessel.TUG_AND_TOW,
            category_of_vessel_registry=Applicability.CategoryOfVesselRegistry.DOMESTIC,
            thickness_of_ice_capability=1,
            vessel_performance="Your boat should be the best of the best",
            logical_connectives=logical_connectives,
        )
        applicability.save()
        VesselsMeasurements.objects.create(
            applicability=applicability,
            vessels_characteristics=VesselsMeasurements.VesselsCharacteristics.LENGTH_OVERALL,
            comparison_operator=VesselsMeasurements.ComparisonOperator.GREATER_THAN,
            vessels_characteristics_value=Decimal("1.1"),
            vessels_characteristics_unit=VesselsMeasurements.VesselsCharacteristicsUnit.METRE,
        )
        VesselsMeasurements.objects.create(
            applicability=applicability,
            vessels_characteristics=VesselsMeasurements.VesselsCharacteristics.LENGTH_OVERALL,
            comparison_operator=VesselsMeasurements.ComparisonOperator.GREATER_THAN,
            vessels_characteristics_value=Decimal("1.2"),
            vessels_characteristics_unit=VesselsMeasurements.VesselsCharacteristicsUnit.METRE,
        )

        assert (
            str(applicability) == f"In ballast, "
            f"Liquid or Livestock or Heavy Lift, "
            f"Imdg Code Class 1 Div 1 1 or Harmful Substances In Packaged Form or Imdg Code Class 3, "
            f"Tug And Tow, "
            f"Domestic, "
            f"Thickness of ice capability: 1, "
            f"Your boat should be the …, "
            f"Length Overall > 1.1 Metre {logical_operator} Length Overall > 1.2 Metre"
        )


class TestVesselsCharacteristicsValue:
    @pytest.mark.parametrize(
        "value",
        [
            "9999999.999",
            0,
        ],
    )
    def test_accepts(self, value):
        assert (
            VesselsMeasurements(
                vessels_characteristics_value=Decimal(value)
            ).clean_fields(
                exclude=[
                    "applicability",
                    "vessels_characteristics",
                    "comparison_operator",
                    "vessels_characteristics_unit",
                ]
            )
            == None
        )

    @pytest.mark.parametrize(
        "value,error_codes",
        [
            ("9.0124", ["max_decimal_places"]),
            ("-9.01234", ["min_value", "max_decimal_places"]),
            ("-9.0", ["min_value"]),
            ("12345678.910", ["max_digits"]),
            (12.91, ["max_digits"]),
        ],
    )
    def test_rejects(self, value, error_codes):
        with pytest.raises(ValidationError) as excinfo:
            VesselsMeasurements(
                vessels_characteristics_value=Decimal(value)
            ).clean_fields(
                exclude=[
                    "applicability",
                    "vessels_characteristics",
                    "comparison_operator",
                    "vessels_characteristics_unit",
                ]
            )
        assert {
            field: [error.code for error in error_list]
            for field, error_list in excinfo.value.error_dict.items()
        } == {"vessels_characteristics_value": error_codes}


class TestPilotBoardingPlaceGeometry:
    @pytest.mark.parametrize(
        "value",
        [
            pytest.param([Point(0, 0)], id="point"),
            pytest.param([Polygon.from_bbox((0, 0, 0, 0))], id="polygon"),
            pytest.param([Point(0, 0), Polygon.from_bbox((0, 0, 0, 0))], id="mixed"),
        ],
    )
    def test_accepts(self, value):
        assert (
            PilotBoardingPlace(geometry=GeometryCollection(value)).clean_fields()
            == None
        )

    @pytest.mark.parametrize(
        "value",
        [
            pytest.param([LineString((0, 0), (0, 0))], id="linestring"),
            pytest.param([LinearRing((0, 0), (0, 0), (0, 0), (0, 0))], id="linearring"),
            pytest.param(
                [
                    Point(0, 0),
                    Polygon.from_bbox((0, 0, 0, 0)),
                    LineString((0, 0), (0, 0)),
                    LinearRing((0, 0), (0, 0), (0, 0), (0, 0)),
                ],
                id="mixed",
            ),
        ],
    )
    def test_rejects(self, value):
        with pytest.raises(ValidationError) as excinfo:
            PilotBoardingPlace(geometry=GeometryCollection(value)).clean_fields()
        assert {
            field: [error.code for error in error_list]
            for field, error_list in excinfo.value.error_dict.items()
        } == {"geometry": ["point_or_surface"]}
