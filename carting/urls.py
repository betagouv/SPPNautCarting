from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "pilotage_district/<int:pk>", views.pilotage_district, name="pilotage_district"
    ),
    path(
        "proxy/wms",
        views.wms_proxy,
        kwargs={"wms_url": "https://services.data.shom.fr/INSPIRE/wms/v"},
        name="wms-proxy",
    ),
]
