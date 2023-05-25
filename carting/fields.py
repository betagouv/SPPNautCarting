from django import forms
from django.contrib.postgres.fields import ArrayField


class ChoiceArrayField(ArrayField):
    def formfield(self, **kwargs):
        choice_with_max_len_label = max(
            [choice[1] for choice in self.base_field.choices], key=len
        )
        widget_class_following_choices_length = "choice-array-field-15rem"
        if len(choice_with_max_len_label) > 30:
            widget_class_following_choices_length = "choice-array-field-100pc"
        defaults = {
            "form_class": forms.MultipleChoiceField,
            "choices": self.base_field.choices,
            "widget": forms.CheckboxSelectMultiple(
                # FIXME : Les classes s'appliquent sur les labels des checkbox en plus du parent
                attrs={"class": widget_class_following_choices_length},
            ),
        }
        defaults.update(kwargs)

        return super(ArrayField, self).formfield(**defaults)
