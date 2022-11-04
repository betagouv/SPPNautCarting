"""
Router config for home module
"""
from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path("", RedirectView.as_view(pattern_name="home:ouvrages_by_name")),
    path(
        "tableau/",
        views.tableau,
        name="tableau",
    ),
    path(
        "publication/",
        views.publication_upload,
        name="publication_upload",
    ),
    path(
        "publication-referentiel/",
        views.publication_referentiel,
        name="publication_referentiel",
    ),
    path(
        "publication/<slug:generation_id>/",
        views.publication_display,
        name="publication_display",
    ),
    path(
        "ouvrages-by-date/",
        views.ouvrages_by_date,
        name="ouvrages_by_date",
    ),
    path(
        "ouvrages-by-name/",
        views.ouvrages_by_name,
        name="ouvrages_by_name",
    ),
]
