import logging

from django.contrib.gis import admin

from .models import INSection
from .widgets import CustomOSMWidget

logger = logging.getLogger(__name__)


@admin.register(INSection)
class INSectionAdmin(admin.GISModelAdmin):
    gis_widget = CustomOSMWidget
    ordering = ("numero",)
    list_display = ("__str__", "bpn_id", "ouvrage_name")
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
