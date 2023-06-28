import copy
import logging
from inspect import getmro, isclass
from types import NoneType
from typing import cast

from django import forms
from django.conf import ImproperlyConfigured
from django.contrib import admin
from django.contrib.admin.helpers import AdminForm
from django.contrib.admin.options import InlineModelAdmin
from django.contrib.gis.admin import GISModelAdmin
from django.urls import reverse
from django.utils.html import format_html_join
from tree_queries.models import TreeNode

from .models import OuvrageSection
from .widgets import CustomOSMWidget

logger = logging.getLogger(__name__)


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


class ModelAdminWithFormsetsIncludingInline(admin.ModelAdmin):
    change_form_template = "admin/change_form_with_inlines_in_fieldsets.html"
    fieldsets_and_inlines_ordered = []

    def __init__(self, *args, **kwargs):
        if self.inlines or self.fieldsets:
            raise ImproperlyConfigured(
                f"The class {self.__class__.__name__} inherits from ModelAdminWithFormsetsIncludingInline. It should only define fieldsets_and_inlines_ordered. Inlines and fieldsets won't be displayed \n"
            )

        super().__init__(*args, **kwargs)

    def get_fieldsets(self, *args, **kwargs):
        fieldsets = copy.deepcopy(self.fieldsets_and_inlines_ordered)
        for _, attributes in fieldsets:
            attributes["fields"] = [
                field for field in attributes["fields"] if isinstance(field, str)
            ]
        return fieldsets

    def get_inlines(self, *args, **kwargs):
        return [
            field
            for _, attributes in self.fieldsets_and_inlines_ordered
            for field in attributes["fields"]
            if isclass(field) and InlineModelAdmin in getmro(field)
        ]

    def render_change_form(self, request, context, *args, **kwargs):
        inline_admin_formsets_by_fieldset_name = {}

        for name, attributes in self.fieldsets_and_inlines_ordered:
            inline_admin_formsets_by_fieldset_name[name] = [
                formset
                for field in attributes["fields"]
                if isclass(field) and InlineModelAdmin in getmro(field)
                for formset in context["inline_admin_formsets"]
                if isinstance(formset.opts, field)
            ]

        context.update(
            {
                "inline_admin_formsets_by_fieldset_name": inline_admin_formsets_by_fieldset_name,
            }
        )
        return super().render_change_form(request, context, *args, **kwargs)


class GISModelAdminWithRasterMarine(GISModelAdmin):
    gis_widget = CustomOSMWidget


@admin.register(OuvrageSection)
class OuvrageSectionAdmin(GISModelAdminWithRasterMarine):
    ordering = ("numero",)
    list_display = ("__str__", "bpn_id", "ouvrage_name")
    list_filter = (
        ("geometry", admin.EmptyFieldListFilter),
        "typology",
    )
    search_fields = ("bpn_id", "numero", "content")

    readonly_fields = (
        "bpn_id",
        "numero",
        "content",
        children,
        "parent",
    )
    fields = (
        "numero",
        "bpn_id",
        "parent",
        children,
        "geometry",
        "content",
    )

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
