from django.urls import path

from . import views

urlpatterns = [
    path("", views.DisplayINWithMap.as_view(), name="display_in_with_map"),
    path("<slug:ouvrage>/", views.display_document_xml, name="display_document_xml"),
]
