from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path("", RedirectView.as_view(pattern_name="carting:search_by_position")),
    path("text", views.search_by_text, name="search_by_text"),
    path("position", views.search_by_position, name="search_by_position"),
    path(
        "position/<uuid:root_expanded>/<uuid:expanded>",
        views.search_by_position_details,
        name="search_by_position_details",
    ),
    path(
        "proxy/wms",
        views.wms_proxy,
        kwargs={"wms_url": "https://services.data.shom.fr/INSPIRE/wms/v"},
        name="wms-proxy",
    ),
]
