from django.contrib.gis import admin

from .models import Element


# Register your models here.
@admin.register(Element)
class ElementAdmin(admin.GISModelAdmin):

    ordering = ("id",)

    gis_widget_kwargs = {
        "attrs": {
            "default_lat": 48.6,
            "default_lon": -2.0,
            "default_zoom": 10,
            "display_raw": True,
            "map_srid": 4326,
        }
    }
