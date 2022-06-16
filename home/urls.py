"""
Router config for home module
"""
from django.urls import path

from . import views

urlpatterns = [
    path(
        "",
        views.index,
        name="index",
    ),
    path(
        "publication/",
        views.publication_upload,
        name="publication_upload",
    ),
    path("publication/<slug:generation_id>/", views.publication_display, name="publication_display"),
]
