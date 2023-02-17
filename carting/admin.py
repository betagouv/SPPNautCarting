import logging

from django.contrib import admin
from django.contrib.gis.admin import GISModelAdmin
from django.urls import reverse
from django.utils.html import format_html_join

from .models import OuvrageSection
from .widgets import CustomOSMWidget

logger = logging.getLogger(__name__)


def children(instance):
    children = instance.children.all()

    if not children:
        return "No children"

    return format_html_join(
        ", ",
        '<a href="{}">{}</a>',
        (
            (
                reverse("admin:carting_ouvragesection_change", args=(child.pk,)),
                child,
            )
            for child in children
        ),
    )


@admin.register(OuvrageSection)
class INSectionAdmin(GISModelAdmin):
    gis_widget = CustomOSMWidget
    ordering = ("numero",)
    list_display = ("__str__", "bpn_id", "ouvrage_name")
    list_filter = (("geometry", admin.EmptyFieldListFilter),)
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
