import logging
from typing import cast

from django import forms
from django.contrib import admin
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
        admin_fieldsets = context["adminform"]
        fieldsets_and_inlines_order = (
            admin_fieldsets.model_admin.fieldsets_and_inlines_order
        )

        fieldsets_and_inlines = []
        for fieldset_or_inline in fieldsets_and_inlines_order:
            fieldsets_and_inlines.extend(
                fieldset.name
                for fieldset in admin_fieldsets
                if fieldset.name == fieldset_or_inline
            )
            fieldsets_and_inlines.extend(
                formset
                for formset in admin_inlines_formsets
                if isinstance(formset.opts, fieldset_or_inline)
            )

        fieldsets_and_inlines.extend(
            filter(
                lambda x: x.name not in fieldsets_and_inlines_order,
                admin_fieldsets,
            )
        )
        fieldsets_and_inlines.extend(
            filter(
                lambda x: x.opts.verbose_name not in fieldsets_and_inlines_order,
                admin_inlines_formsets,
            )
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
