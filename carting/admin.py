import logging

from django.conf import settings
from django.contrib.gis import admin, forms, gdal
from django.contrib.gis.geometry import json_regex
from django.contrib.gis.geos import GEOSException, GEOSGeometry
from django.utils import translation

from .models import Element

logger = logging.getLogger(__name__)


class CustomOSMWidget(forms.widgets.BaseGeometryWidget):
    template_name = "gis/openlayers-osm.html"
    default_lon = 5
    default_lat = 47
    default_zoom = 12

    def deserialize(self, value):
        try:
            return GEOSGeometry(value)
        except (GEOSException, ValueError, TypeError) as err:
            print("Error creating geometry from value '%s' (%s)", value, err)
        return None

    class Media:
        css = {
            "all": (
                "https://cdnjs.cloudflare.com/ajax/libs/ol3/4.6.5/ol.css",
                "gis/css/ol3.css",
            )
        }
        js = (
            "https://cdnjs.cloudflare.com/ajax/libs/ol3/4.6.5/ol.js",
            # "gis/js/OLMapWidget.js",
            "OLMapWidget.js",
        )

    def __init__(self, attrs=None):
        super().__init__()
        for key in ("default_lon", "default_lat", "default_zoom"):
            self.attrs[key] = getattr(self, key)
        if attrs:
            self.attrs.update(attrs)

    def serialize(self, value):
        return value.json if value else ""

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        # If a string reaches here (via a validation error on another
        # field) then just reconstruct the Geometry.
        if value and isinstance(value, str):
            value = self.deserialize(value)

        if value:
            # Check that srid of value and map match
            if value.srid and value.srid != self.map_srid:
                try:
                    ogr = value.ogr
                    ogr.transform(self.map_srid)
                    value = ogr
                except gdal.GDALException as err:
                    logger.error(
                        "Error transforming geometry from srid '%s' to srid '%s' (%s)",
                        value.srid,
                        self.map_srid,
                        err,
                    )

        geom_type = gdal.OGRGeomType(self.attrs["geom_type"]).name
        context.update(
            self.build_attrs(
                self.attrs,
                {
                    "name": name,
                    "module": "geodjango_%s" % name.replace("-", "_"),  # JS-safe
                    "serialized": self.serialize(value),
                    "geom_type": "Geometry" if geom_type == "Unknown" else geom_type,
                    "STATIC_URL": settings.STATIC_URL,
                    "LANGUAGE_BIDI": translation.get_language_bidi(),
                    **(attrs or {}),
                },
            )
        )
        return context


@admin.register(Element)
class ElementAdmin(admin.GISModelAdmin):
    ordering = ("bpn_id",)
    gis_widget = CustomOSMWidget

    search_fields = ("xpath", "bpn_id", "numero")

    gis_widget_kwargs = {
        "attrs": {
            "default_lat": 48.6,
            "default_lon": -2.0,
            "default_zoom": 10,
            "display_raw": True,
            "map_srid": 4326,
        }
    }
