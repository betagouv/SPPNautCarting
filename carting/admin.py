from django.contrib.gis import admin, forms
from django.contrib.gis.geometry import json_regex
from django.db import models

from carting.widgets import CustomOSMWidget, CustomOSMWidget2

from .models import Element


# Register your models here.
@admin.register(Element)
class ElementAdmin(admin.GISModelAdmin):
    pass

    # gis_widget = CustomOSMWidget2
    gis_widget_kwargs = {
        "attrs": {
            "default_lat": 48.6,
            "default_lon": -2.0,
            "default_zoom": 10,
            "display_raw": True,
            "map_srid": 4326,
        }
    }

    # formfield_overrides = {
    #     models.TextField: {
    #         "widget": admin.OSMWidget(attrs={"map_width": 800, "map_height": 500})
    #     },
    # }
