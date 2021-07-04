import os
import sys

from dotenv import load_dotenv

load_dotenv()

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PROJECT_PATH))

DEBUG = True
SITE_URL = os.getenv("SITE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")

ADMINS = (("Sobolev Andrey", "email.asobolev@gmail.com"),)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": POSTGRES_DB,
        "USER": POSTGRES_USER,
        "PASSWORD": POSTGRES_PASSWORD,
        "HOST": POSTGRES_HOST,
        "PORT": POSTGRES_PORT,
    }
}
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

STATIC_ROOT = os.path.join(PROJECT_PATH, "static")
STATIC_URL = "/static/"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.csrf",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.request",
                "context_processors.common",
            ],
            "loaders": [
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
        },
        "DIRS": [os.path.join(PROJECT_PATH, "templates")],
    },
]

MIDDLEWARE = (
    "django.middleware.locale.LocaleMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
)

USE_I18N = True
USE_L10N = True
TIME_ZONE = "Europe/Moscow"
ROOT_URLCONF = "urls"

INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "encrypt",
)

ALLOWED_HOSTS = ["*"]
