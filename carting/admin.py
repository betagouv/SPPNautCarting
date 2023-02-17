import logging

from django.contrib import admin
from django.contrib.gis.admin import GISModelAdmin

from .models import OuvrageSection
from .widgets import CustomOSMWidget

logger = logging.getLogger(__name__)


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
    )
    fields = (
        "bpn_id",
        "numero",
        "content",
        "geometry",
    )
