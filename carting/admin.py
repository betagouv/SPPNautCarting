import logging

from django.contrib import admin
from django.contrib.gis.admin import GISModelAdmin
from django.urls import reverse
from django.utils.html import format_html_join
from tree_queries.models import TreeNode

from .models import BDGS, OuvrageSection
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


@admin.register(OuvrageSection)
class OuvrageSectionAdmin(GISModelAdmin):
    gis_widget = CustomOSMWidget

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
        "bdgs_object",
        "geometry",
        "content",
    )

    raw_id_fields = ("bdgs_object",)
    ordering = ("numero",)
    list_display = ("__str__", "bpn_id", "ouvrage_name")
    list_filter = (
        ("geometry", admin.EmptyFieldListFilter),
        ("bdgs_object", admin.EmptyFieldListFilter),
    )
    search_fields = ("bpn_id", "numero", "content")
    change_form_template = "widgets/text_with_map.html"

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(BDGS)
class BDGSAdmin(GISModelAdmin):
    gis_widget = CustomOSMWidget
    list_display = ("inspire_id", "category")
    search_fields = ("inspire_id", "category")

    readonly_fields = ("inspire_id", "category", "raw", "geometry")

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
