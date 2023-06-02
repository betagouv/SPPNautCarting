import logging
from types import NoneType
from typing import cast

from django import forms
from django.contrib import admin
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


class Toto:
    def __init__(self, inlines=None, fields=None):
        self.inlines = inlines
        self.fields = fields
        self.formsets = []

    def retrieve_formsets_and_fieldsets(self, request, admin):
        print(type(admin), admin)
        if self.inlines:
            admin.inlines = self.inlines

            formsets = []
            inline_instances = []

            for formset, inline in admin.get_formsets_with_inlines(request, None):
                formsets.append(formset)
                inline_instances.append(inline)

            self.formsets = admin.get_inline_formsets(
                request, formsets, inline_instances, obj=None
            )

        # self.fieldsets = [admin.get_form()]

    @property
    def coucou(self):
        print(self.formsets)
        return self.formsets

    toto = "coucou"


class ModelAdminWithOrderedFormsets(admin.ModelAdmin):
    change_form_template = "admin/change_form_with_ordered_formsets.html"
    fieldsets_and_inlines_order = ()

    def render_change_form(self, request, context, *args, **kwargs):
        context.update(
            {
                "fieldsets_and_inlines": self._get_fieldsets_and_inlines(
                    context, request
                ),
            }
        )
        return super().render_change_form(request, context, *args, **kwargs)

    def _get_fieldsets_and_inlines(self, context, request):
        admin_inlines_formsets = cast(
            list[forms.BaseInlineFormSet],
            context["inline_admin_formsets"],
        )
        adminform = cast(AdminForm, context["adminform"])
        fieldsets_and_inlines_order = adminform.model_admin.fieldsets_and_inlines_order

        fieldsets_and_inlines = []
        for fieldset_or_inline in fieldsets_and_inlines_order:
            match fieldset_or_inline:
                case Toto():
                    fieldset_or_inline.retrieve_formsets_and_fieldsets(request, self)
                    fieldsets_and_inlines.extend([fieldset_or_inline])
                case str() | NoneType():
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
