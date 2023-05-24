from django import forms
from django.contrib.postgres.fields import ArrayField


class ChoiceArrayField(ArrayField):
    def __init__(self, *args, widget_class="choice-array-field", **kwargs):
        self.widget_class = widget_class
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            "form_class": forms.MultipleChoiceField,
            "choices": self.base_field.choices,
            "widget": forms.CheckboxSelectMultiple(
                # FIXME : Les classes s'appliquent sur les labels des checkbox en plus du parent
                attrs={"class": self.widget_class},
            ),
        }
        defaults.update(kwargs)

        return super(ArrayField, self).formfield(**defaults)
