import logging

from django.contrib.gis import admin

from .models import INSection
from .widgets import CustomOSMWidget

logger = logging.getLogger(__name__)


@admin.register(INSection)
class ElementAdmin(admin.GISModelAdmin):
    ordering = ("numero",)
    list_display = ("__str__", "bpn_id", "ouvrage_name")
    gis_widget = CustomOSMWidget
    search_fields = ("bpn_id", "numero", "content")
