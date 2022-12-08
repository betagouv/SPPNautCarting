import pytest


@pytest.fixture(autouse=True)
def disable_whitenoise(settings):
    settings.STATICFILES_STORAGE = (
        "django.contrib.staticfiles.storage.StaticFilesStorage"
    )
