from django.db import models

from carting.fields import ChoiceArrayField


class TestChoiceArrayField:
    def test_short(self):
        field = ChoiceArrayField(
            base_field=models.TextField(
                choices=[("", "a" * 30)],
            )
        )
        assert (
            field.formfield().widget.attrs["class"]
            == "choice-array-field choice-array-field-several-columns"
        )

    def test_long(self):
        field = ChoiceArrayField(
            base_field=models.TextField(
                choices=[("", "a" * 31)],
            )
        )
        assert (
            field.formfield().widget.attrs["class"]
            == "choice-array-field choice-array-field-one-column"
        )
