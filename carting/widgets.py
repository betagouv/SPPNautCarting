from django.contrib.gis import forms


class CustomOSMWidget(forms.widgets.BaseGeometryWidget):
    template_name = "admin/custom-openlayers.html"
    default_lon = -2
    default_lat = 48.6
    default_zoom = 12
    dataset_epsg = "EPSG:4326"
    map_epsg = "EPSG:3857"
    display_raw = True

    class Media:
        css = {
            "all": (
                "https://cdnjs.cloudflare.com/ajax/libs/ol3/4.6.5/ol.css",
                "gis/css/ol3.css",
            )
        }
        js = (
            "https://cdnjs.cloudflare.com/ajax/libs/ol3/4.6.5/ol.js",
            "admin-map-widget.js",
        )

    def __init__(self, attrs=None):
        super().__init__(attrs)

        for key in (
            "dataset_epsg",
            "map_epsg",
            "default_zoom",
            "default_lat",
            "default_lon",
            "display_raw",
        ):
            self.attrs[key] = getattr(self, key)
        if attrs:
            self.attrs.update(attrs)

    def serialize(self, value):
        return value.json if value else ""
