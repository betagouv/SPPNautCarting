import logging

from django.contrib import admin
from django.contrib.gis.admin import GISModelAdmin

from carting.forms import OuvrageSectionForm

from .models import BDGS, OuvrageSection
from .widgets import CustomOSMWidget

logger = logging.getLogger(__name__)


@admin.register(OuvrageSection)
class OuvrageSectionAdmin(GISModelAdmin):
    gis_widget = CustomOSMWidget
    ordering = ("numero",)
    list_display = ("__str__", "bpn_id", "ouvrage_name")
    list_filter = (("geometry", admin.EmptyFieldListFilter),)
    search_fields = ("bpn_id", "numero", "content")
    form = OuvrageSectionForm

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(BDGS)
class BDGSAdmin(GISModelAdmin):
    # ordering = ("numero",)
    gis_widget = CustomOSMWidget
    list_display = ("inspire_id", "category")
    search_fields = ("inspire_id", "category")

    # readonly_fields = ("inspire_id",)
