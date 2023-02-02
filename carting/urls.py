from django.urls import path

from . import views

urlpatterns = [
    path("", views.frontend_carting, name="frontend_carting"),
]
