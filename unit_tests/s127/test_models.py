from decimal import Decimal

import pytest
from django.core.exceptions import ValidationError

from s127.models.information_type import VesselsMeasurements


class TestVesselsCharacteristicsValue:
    @pytest.mark.parametrize(
        "value",
        [
            "9999999.999",
            0,
        ],
    )
    def test_accepts(self, value):
        VesselsMeasurements(vessels_characteristics_value=Decimal(value)).clean_fields(
            exclude=[
                "applicability",
                "vessels_characteristics",
                "comparison_operator",
                "vessels_characteristics_unit",
            ]
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
