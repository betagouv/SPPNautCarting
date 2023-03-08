from pathlib import Path

import sentry_sdk
from decouple import config
from sentry_sdk.integrations.django import DjangoIntegration

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", cast=bool)

ALLOWED_HOSTS = config(
    "ALLOWED_HOSTS", cast=lambda v: [s.strip() for s in v.split(",")]
)

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
    "django.contrib.gis",
    "django_extensions",
    "gisserver",
    "spo",
    "carting",
]

if DEBUG:
    INSTALLED_APPS.extend(
        [
            "django_browser_reload",
        ]
    )

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
if "django_browser_reload" in INSTALLED_APPS:
    MIDDLEWARE.extend(
        [
            "django_browser_reload.middleware.BrowserReloadMiddleware",
        ]
    )

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "spo.context_processors.menu",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": config("POSTGRESQL_ADDON_DB"),
        "USER": config("POSTGRESQL_ADDON_USER"),
        "PASSWORD": config("POSTGRESQL_ADDON_PASSWORD"),
        "HOST": config("POSTGRESQL_ADDON_HOST"),
        "PORT": config("POSTGRESQL_ADDON_PORT"),
    }
}

# Static files
STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_URL = "static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
    BASE_DIR / "compiled_static",
]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
WHITENOISE_KEEP_ONLY_HASHED_FILES = True

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

SECURE_SSL_REDIRECT = config("SECURE_SSL_REDIRECT", cast=bool)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "skip_staticfiles": {
            "()": "core.filters.SkipStaticFilter",
        },
    },
    "formatters": {
        "console": {
            "()": "django.utils.log.ServerFormatter",
            "format": "{levelname}:{name}: {message}",
            "style": "{",
        },
        "django.server": {
            "()": "django.utils.log.ServerFormatter",
            "format": "{message}\n--------",
            "style": "{",
        },
    },
    "handlers": {
        "django.server": {
            "class": "logging.StreamHandler",
            "filters": ["skip_staticfiles"],
            "formatter": "django.server",
        },
    },
    "root": {
        "level": "WARNING",
    },
    "loggers": {
        "django.server": {
            "handlers": ["django.server"],
        }
    },
}


GENERATOR_SERVICE_HOST = config("GENERATOR_SERVICE_HOST")
GENERATOR_USERNAME = config("GENERATOR_USERNAME")
GENERATOR_PASSWORD = config("GENERATOR_PASSWORD")

DATASHOM_WMS_KEY = config("DATASHOM_WMS_KEY")
DATASHOM_WMS_USERNAME = config("DATASHOM_WMS_USERNAME")
DATASHOM_WMS_PASSWORD = config("DATASHOM_WMS_PASSWORD")

sentry_sdk.init(
    dsn=config("SENTRY_DSN"),
    integrations=[DjangoIntegration()],
    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True,
    # By default the SDK will try to use the SENTRY_RELEASE
    # environment variable, or infer a git commit
    # SHA as release, however you may want to set
    # something more human-readable.
    # release="myapp@1.0.0",
)
LOGIN_REDIRECT_URL = "spo:ouvrages_by_name"
LANGUAGE_CODE = "fr"

SHELL_PLUS_PRINT_SQL = True
GDAL_LIBRARY_PATH = config("GDAL_LIBRARY_PATH", default=None)
GEOS_LIBRARY_PATH = config("GEOS_LIBRARY_PATH", default=None)
