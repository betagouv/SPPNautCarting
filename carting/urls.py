from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "proxy/wms",
        views.wms_proxy,
        kwargs={"wms_url": "https://services.data.shom.fr/INSPIRE/wms/v"},
        name="wms-proxy",
    ),
]
