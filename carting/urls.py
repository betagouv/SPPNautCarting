from django.urls import path

from . import views

urlpatterns = [
    path("<slug:ouvrage>/", views.display_document_xml, name="display_document_xml"),
]
