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
        views.publication_generation_in_progress,
        name="publication_generation_in_progress",
    ),
    path(
        "publication/<slug:generation_id>/ended/",
        views.publication_generation_ended,
        name="publication_generation_ended",
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
    path(
        "display-document-xml/",
        views.display_document_xml,
        name="display_document_xml",
    ),
]
