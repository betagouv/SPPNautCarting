import nested_admin
from django import forms
from django.contrib.contenttypes.models import ContentType

import s100.models


class MyArticleAdminForm(forms.ModelForm):
    def full_clean(self) -> None:
        super().full_clean()
        # if self.instance.name != "f":
        # raise KeyError(self.instance.content_type)
        self.instance.validate_constraints()

    # def clean(self):
    #     cleaned_data = super().clean()
    #     # try:
    #     # if self.instance.name != "f":
    #     #     raise KeyError(self.instance)
    #     # foo = self.instance.validate_constraints()
    #     # except ValidationError as e:
    #     # print(e)
    #     return cleaned_data


class MyFormSet(nested_admin.NestedBaseGenericInlineFormSet):
    def clean(self):
        raise KeyError("MyFormSet")
        super().clean()


class FeatureNameInline(nested_admin.NestedGenericTabularInline):
    model = s100.models.FeatureName
    # form = MyArticleAdminForm
    # formset = MyFormSet
    is_sortable = False
    min_num = 1
    extra = 0


class InformationInline(nested_admin.NestedGenericStackedInline):
    model = s100.models.Information
    fields = ("headline", "text")
    # FIXME: Why did we decide to make it a 1 when the spec says [0..*] ?
    extra = 0
    min_num = 1
    max_num = 1
    is_sortable = False


class TextContentInline(nested_admin.NestedGenericStackedInline):
    model = s100.models.TextContent
    inlines = [InformationInline]
    extra = 0
    max_num = 1
    is_sortable = False
    # classes = ["collapse"] FIXME
