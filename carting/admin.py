import copy
from itertools import tee, filterfalse
from inspect import getmro, isclass
import logging
from types import NoneType
from typing import cast

from django import forms
from django.conf import ImproperlyConfigured
from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin
from django.contrib.admin.helpers import AdminForm
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

    def _partition_fieldsets_and_inlines(self, fields_and_inlines):
        def coucou(field_or_inline):
            return isinstance(field_or_inline, str)

        t1, t2 = tee(fields_and_inlines)

        return filterfalse(coucou, t1), filter(coucou, t2)

    def get_fieldsets(self, *args, **kwargs):
        fieldsets = copy.deepcopy(self.fieldsets_and_inlines_ordered)

        for _, attributes in fieldsets:
            _, fields = self._partition_fieldsets_and_inlines(attributes["fields"])
            attributes["fields"] = list(fields)

        return fieldsets

    def get_inlines(self, *args, **kwargs):
        return [
            inline
            for _, attributes in self.fieldsets_and_inlines_ordered
            for inlines, _ in self._partition_fieldsets_and_inlines(
                attributes["fields"]
            )
            for inline in inlines
        ]

        for _, attributes in self.fieldsets_and_inlines_ordered:
            inlines, _ = self._partition_fieldsets_and_inlines(attributes["fields"])
            attributes["fields"] = list(inlines)

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


class ModelAdminWithOrderedFormsets(admin.ModelAdmin):
    change_form_template = "admin/change_form_with_ordered_formsets.html"
    fieldsets_and_inlines_order = ()

    def render_change_form(self, request, context, *args, **kwargs):
        context.update(
            {"fieldsets_and_inlines": self._get_fieldsets_and_inlines(context)}
        )
        return super().render_change_form(request, context, *args, **kwargs)

    def _get_fieldsets_and_inlines(self, context):
        admin_inlines_formsets = cast(
            list[forms.BaseInlineFormSet],
            context["inline_admin_formsets"],
        )
        adminform = cast(AdminForm, context["adminform"])
        fieldsets_and_inlines_order = adminform.model_admin.fieldsets_and_inlines_order

        fieldsets_and_inlines = []
        for fieldset_or_inline in fieldsets_and_inlines_order:
            match fieldset_or_inline:
                case str() | None:
                    fieldsets_and_inlines.extend(
                        fieldset
                        for fieldset in adminform
                        if fieldset.name == fieldset_or_inline
                    )
                case _:
                    fieldsets_and_inlines.extend(
                        formset
                        for formset in admin_inlines_formsets
                        if isinstance(formset.opts, fieldset_or_inline)
                    )

        fieldsets_and_inlines.extend(
            fieldset
            for fieldset in adminform
            if fieldset.name not in fieldsets_and_inlines_order
        )

        fieldsets_and_inlines.extend(
            formset
            for formset in admin_inlines_formsets
            if type(formset.opts) not in fieldsets_and_inlines_order
        )

        return fieldsets_and_inlines


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
