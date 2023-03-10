import typing

from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import URLPattern, URLResolver, include, path

URL = typing.Union[URLPattern, URLResolver]
URLList = typing.List[URL]

urlpatterns: URLList = [
    path("admin/", admin.site.urls),
    path("accounts/login/", auth_views.LoginView.as_view()),
    path("accounts/logout/", auth_views.logout_then_login, name="logout"),
    path("", include(("spo.urls", "users"), namespace="spo")),
    path("carting/", include(("carting.urls", "carting"), namespace="carting")),
]

if "django_browser_reload" in settings.INSTALLED_APPS:
    urlpatterns.extend(
        [
            path("__reload__/", include("django_browser_reload.urls")),
        ]
    )
