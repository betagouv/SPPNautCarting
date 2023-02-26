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
    path("", include(("home.urls", "users"), namespace="home")),
    path("carting/", include(("carting.urls", "carting"), namespace="carting")),
]

<<<<<<< HEAD
if "django_browser_reload" in settings.INSTALLED_APPS:
=======
if settings.DEBUG:
>>>>>>> ddf8f61 (Reload tabs when Python code or templates change)
    urlpatterns.extend(
        [
            path("__reload__/", include("django_browser_reload.urls")),
        ]
    )
