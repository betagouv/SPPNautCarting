from contextlib import suppress

import pytest


@pytest.fixture(autouse=True)
def disable_whitenoise(settings):
    settings.STATICFILES_STORAGE = (
        "django.contrib.staticfiles.storage.StaticFilesStorage"
    )


@pytest.fixture(autouse=True)
def disable_debug_toolbar(settings):
    with suppress(ValueError):
        settings.MIDDLEWARE.remove("debug_toolbar.middleware.DebugToolbarMiddleware")
