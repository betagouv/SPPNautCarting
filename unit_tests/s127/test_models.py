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

from s127.models import (
    Applicability,
    ContactDetails,
    PilotBoardingPlace,
    Telecommunications,
    VesselsMeasurements,
)
from s127.models.shared import CategoryOfVessel


class TestVesselsMeasurementsStr:
    def test_empty(self):
        assert str(VesselsMeasurements()) == "VesselsMeasurements object (None)"

    @pytest.mark.parametrize(
        "value_input, value_output",
        [
            ("1.100", "1.1"),
            ("50", "50"),
            ("50.60", "50.6"),
        ],
    )
    @pytest.mark.django_db
    def test_basic(self, value_input, value_output):
        vessels_measurements = VesselsMeasurements.objects.create(
            applicability=Applicability.objects.create(),
            vessels_characteristics=VesselsMeasurements.VesselsCharacteristics.LENGTH_OVERALL,
            comparison_operator=VesselsMeasurements.ComparisonOperator.GREATER_THAN,
            vessels_characteristics_value=Decimal(value_input),
            vessels_characteristics_unit=VesselsMeasurements.VesselsCharacteristicsUnit.METRE,
        )
        assert str(vessels_measurements) == f"Length Overall > {value_output} Metre"

        str_from_memory = str(vessels_measurements)
        vessels_measurements.refresh_from_db()
        str_from_db = str(vessels_measurements)
        assert str_from_db == str_from_memory


class TestApplicabilityStr:
    def test_empty(self):
        assert str(Applicability()) == "Applicability object (None)"

    @pytest.mark.django_db
    def test_empty_saved(self):
        applicability = Applicability.objects.create()
        assert str(applicability) == f"Applicability object ({applicability.pk})"

    @pytest.mark.django_db
    def test_with_in_ballast_true(self):
        applicability = Applicability.objects.create(in_ballast=True)
        assert str(applicability) == "In ballast"

    @pytest.mark.django_db
    def test_with_in_ballast_false(self):
        applicability = Applicability.objects.create(in_ballast=False)
        assert str(applicability) == "Not in ballast"

    @pytest.mark.django_db
    def test_with_category_of_cargo(self):
        applicability = Applicability.objects.create(
            category_of_cargo=[Applicability.CategoryOfCargo.LIQUID]
        )
        assert str(applicability) == "Liquid"

    @pytest.mark.django_db
    def test_with_multiple_category_of_cargo(self):
        applicability = Applicability.objects.create(
            category_of_cargo=[
                Applicability.CategoryOfCargo.LIQUID,
                Applicability.CategoryOfCargo.LIVESTOCK,
                Applicability.CategoryOfCargo.HEAVY_LIFT,
            ]
        )
        assert str(applicability) == "Liquid or Livestock or Heavy Lift"

    @pytest.mark.django_db
    def test_with_dangerous_or_hazardous_cargo(self):
        applicability = Applicability.objects.create(
            category_of_dangerous_or_hazardous_cargo=[
                Applicability.CategoryOfDangerousOrHazardousCargo.IMDG_CODE_CLASS_1_DIV_1_1
            ]
        )
        assert (
            str(applicability)
            == "Explosives, Division 1: substances and articles which have a mass explosion hazard"
        )

    @pytest.mark.django_db
    def test_with_multiple_dangerous_or_hazardous_cargo(self):
        applicability = Applicability.objects.create(
            category_of_dangerous_or_hazardous_cargo=[
                Applicability.CategoryOfDangerousOrHazardousCargo.IMDG_CODE_CLASS_1_DIV_1_1,
                Applicability.CategoryOfDangerousOrHazardousCargo.HARMFUL_SUBSTANCES_IN_PACKAGED_FORM,
                Applicability.CategoryOfDangerousOrHazardousCargo.IMDG_CODE_CLASS_3,
            ]
        )
        assert (
            str(applicability)
            == "Explosives, Division 1: substances and articles which have a mass explosion hazard or Harmful Substances In Packaged Form or flammable liquids"
        )

    @pytest.mark.django_db
    def test_with_category_of_vessel(self):
        applicability = Applicability.objects.create(
            category_of_vessel=CategoryOfVessel.TUG_AND_TOW
        )
        assert str(applicability) == "Tug And Tow"

    @pytest.mark.django_db
    def test_with_category_of_vessel_registry(self):
        applicability = Applicability.objects.create(
            category_of_vessel_registry=Applicability.CategoryOfVesselRegistry.DOMESTIC
        )
        assert str(applicability) == "Domestic"

    @pytest.mark.django_db
    def test_with_thickness_of_ice_capability(self):
        applicability = Applicability.objects.create(thickness_of_ice_capability=1)
        assert str(applicability) == "Thickness of ice capability: 1"

    @pytest.mark.django_db
    def test_with_vessel_performance(self):
        applicability = Applicability.objects.create(vessel_performance="Cool boat")
        assert str(applicability) == "Cool boat"

    @pytest.mark.django_db
    def test_with_vessel_performance_greather_than_25_char(self):
        applicability = Applicability.objects.create(
            vessel_performance="Your boat should be the best of the best"
        )
        assert str(applicability) == "Your boat should be the …"

    @pytest.mark.django_db
    def test_with_vessels_measurements(self):
        applicability = Applicability.objects.create()
        VesselsMeasurements.objects.create(
            applicability=applicability,
            vessels_characteristics=VesselsMeasurements.VesselsCharacteristics.LENGTH_OVERALL,
            comparison_operator=VesselsMeasurements.ComparisonOperator.GREATER_THAN,
            vessels_characteristics_value=Decimal("1.1"),
            vessels_characteristics_unit=VesselsMeasurements.VesselsCharacteristicsUnit.METRE,
        )
        assert str(applicability) == "Length Overall > 1.1 Metre"

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
        applicability = Applicability.objects.create(
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
            str(applicability) == "In ballast, "
            "Liquid or Livestock or Heavy Lift, "
            "Explosives, Division 1: substances and articles which have a mass explosion hazard or Harmful Substances In Packaged Form or flammable liquids, "
            "Tug And Tow, "
            "Domestic, "
            "Thickness of ice capability: 1, "
            "Your boat should be the …, "
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


class TestContactDetailsMMSICode:
    @pytest.mark.parametrize(
        "value",
        [
            "123456789",
            "",
            "000000000",
        ],
    )
    def test_accepts(self, value):
        assert (
            ContactDetails(mmsi_code=value).clean_fields(exclude=["language"]) == None
        )

    @pytest.mark.parametrize(
        "value",
        [
            000000000,
            "coucou",
            "12345678",
            "1234561.8",
            "1234567810",
        ],
    )
    def test_rejects(self, value):
        with pytest.raises(ValidationError) as excinfo:
            ContactDetails(mmsi_code=value).clean_fields(exclude=["language"])

        assert {
            field: [error.code for error in error_list]
            for field, error_list in excinfo.value.error_dict.items()
        } == {"mmsi_code": ["invalid"]}


class TestTelecommunicationsStr:
    def test_empty(self):
        assert str(Telecommunications()) == "Telecommunications object (None)"

    def test_telecommunication_identifier(self):
        assert str(Telecommunications(telecommunication_identifier="a")) == "a"

    def test_one_telecommunication_service(self):
        assert (
            str(
                Telecommunications(
                    telecommunication_identifier="a",
                    telecommunication_service=[
                        Telecommunications.TelecommunicationService.VOICE
                    ],
                )
            )
            == "Voice: a"
        )

    def test_several_telecommunication_service(self):
        assert (
            str(
                Telecommunications(
                    telecommunication_identifier="a",
                    telecommunication_service=[
                        Telecommunications.TelecommunicationService.VOICE,
                        Telecommunications.TelecommunicationService.SMS,
                        Telecommunications.TelecommunicationService.FACSIMILE,
                    ],
                )
            )
            == "Voice/Sms/Facsimile: a"
        )
