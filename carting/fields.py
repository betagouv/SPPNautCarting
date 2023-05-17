from django import forms
from django.contrib.postgres.fields import ArrayField


class ChoiceArrayField(ArrayField):
    def formfield(self, **kwargs):
        defaults = {
            "form_class": forms.MultipleChoiceField,
            "choices": self.base_field.choices,
            "widget": forms.CheckboxSelectMultiple(
                # FIXME : Les classes s'appliquent sur les labels des checkbox en plus du parent
                attrs={"class": "choice-array-field"},
            ),
        }
        defaults.update(kwargs)

        return super(ArrayField, self).formfield(**defaults)
