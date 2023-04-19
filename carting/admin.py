import logging

from django.contrib import admin
from django.contrib.gis.admin import GISModelAdmin
from django.urls import reverse
from django.utils.html import format_html_join
from tree_queries.models import TreeNode

from .models import OuvrageSection, PilotageDistrict
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


@admin.register(PilotageDistrict)
class PilotageDistrictadmin(GISModelAdmin):
    list_display = ("id",)
