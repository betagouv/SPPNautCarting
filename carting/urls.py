from django.urls import path

from . import views

urlpatterns = [
    path("", views.display_in_with_map, name="display_in_with_map"),
]
