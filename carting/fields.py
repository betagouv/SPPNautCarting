from django import forms
from django.contrib.postgres.fields import ArrayField


class ChoiceArrayField(ArrayField):
    def formfield(self, **kwargs):
        max_label_length = max(len(label) for value, label in self.base_field.choices)
        columns_widget_class = "choice-array-field-several-columns"
        if max_label_length > 30:
            columns_widget_class = "choice-array-field-one-column"

        defaults = {
            "form_class": forms.MultipleChoiceField,
            "choices": self.base_field.choices,
            "widget": forms.CheckboxSelectMultiple(
                # FIXME : Les classes s'appliquent sur chaque input[checkbox] en plus du div les contenant toutes
                attrs={"class": "choice-array-field " + columns_widget_class},
            ),
        }
        defaults.update(kwargs)

        return super(ArrayField, self).formfield(**defaults)
