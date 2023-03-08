from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("proxy", views.proxy, name="proxy"),
    path("wfs/sections/", views.OuvrageSectionWFSView.as_view()),
]
