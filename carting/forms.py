from django import forms
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html_join
from tree_queries.models import TreeNode

from carting.models import BDGS, OuvrageSection


def children(instance: TreeNode):
    children = instance.children.all()

    if not children:
        return "No children"

    return format_html_join(
        ", ",
        '<a href="{}">{}</a>',
        (
            (
                reverse(
                    f"admin:{instance._meta.app_label}_{instance._meta.model_name}_change",
                    args=(child.pk,),
                ),
                child,
            )
            for child in children
        ),
    )


class TextInputWithMap(forms.TextInput):
    template_name = "widgets/text_with_map.html"


class OuvrageSectionForm(forms.ModelForm):
    # readonly_fields = (
    #     "bpn_id",
    #     "numero",
    #     "content",
    #     children,
    #     "parent",
    # )

    class Meta:
        model = OuvrageSection
        widgets = {"bdgs_object": TextInputWithMap}
        fields = (
            "numero",
            "bpn_id",
            "parent",
            "bdgs_object",
            # "children",
            "geometry",
            "content",
        )
