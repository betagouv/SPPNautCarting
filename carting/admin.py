import logging

from django.contrib.gis import admin

from .models import Element
from .widgets import CustomOSMWidget

logger = logging.getLogger(__name__)


@admin.register(Element)
class ElementAdmin(admin.GISModelAdmin):
    ordering = ("bpn_id",)
    gis_widget = CustomOSMWidget
    search_fields = ("xpath", "bpn_id", "numero")
