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

from s127.models.information_type import VesselsMeasurements
from s127.models.organisation_contact_area import PilotBoardingPlace


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
