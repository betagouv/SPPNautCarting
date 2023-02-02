from django.contrib.gis import forms
from django.contrib.gis.geometry import json_regex


class CustomOSMWidget(forms.widgets.OSMWidget):
    map_srid = 4326
    default_lat = 48.6
    default_lon = -2.0
    default_zoom = 10
    display_raw = True


class CustomOSMWidget2(forms.widgets.OpenLayersWidget):
    """
    An OpenLayers/OpenStreetMap-based widget.
    """

    template_name = "gis/openlayers-osm.html"
    default_lat = 48.6
    default_lon = -2.0
    default_zoom = 10
    display_raw = True
    map_srid = 4326

    def __init__(self, attrs=None):
        super().__init__()
        for key in (
            "default_lon",
            "default_lat",
            "default_zoom",
            "map_srid",
            "display_raw",
        ):
            self.attrs[key] = getattr(self, key)
        if attrs:
            self.attrs.update(attrs)

    def serialize(self, value):
        print("serialize", value, value.srid if value else "")
        return value.json if value else ""

    def deserialize(self, value):
        geom = super().deserialize(value)
        print("deserialize", value, self.map_srid, geom.srid)
        # GeoJSON assumes WGS84 (4326). Use the map's SRID instead.
        if geom and json_regex.match(value) and self.map_srid != 4326:
            print("MATCH and self.map_srid != 4326")
            geom.srid = self.map_srid
        return geom
