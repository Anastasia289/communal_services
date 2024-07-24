import os
from pathlib import Path

from django.core.management import utils
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY", default=utils.get_random_secret_key())

DEBUG = os.environ.get("DEBUG") == "True"

ALLOWED_HOSTS = []

AUTH_USER_MODEL = "users.CustomUser"

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "django_celery_beat",
    "drf_yasg",
    "celery",
    "rest_framework",
    "rest_framework_simplejwt",
    "rest_framework.authtoken",
    "djoser",
    "django_filters",
    "users",
    "api",
    "services",
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "backend.wsgi.application"

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB", "django"),
        "USER": os.getenv("POSTGRES_USER", "django"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD", ""),
        "HOST": os.getenv("DB_HOST", ""),
        "PORT": os.getenv("DB_PORT", 5432),
    }
}


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


LLANGUAGE_CODE = "ru-RU"

TIME_ZONE = "Europe/Moscow"

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "collected_static"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "/media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
}

DJOSER = {
    "LOGIN_FIELD": "username",
    "SERIALIZERS": {
        "current_user": "api.serializers.CustomUserSerializer",
        "user": "api.serializers.CustomUserSerializer",
        "user_create": "api.serializers.CustomUserCreateSerializer",
    },
    "PERMISSIONS": {
        "user": ["rest_framework.permissions.AllowAny"],
        "user_list": ["rest_framework.permissions.AllowAny"],
    },
    "HIDE_USERS": False,
}

CORS_ALLOW_ALL_ORIGINS = True


# CELERY_BROKER_URL = "redis://localhost:6379"  # Пример URL Redis-брокера
# CELERY_RESULT_BACKEND = (
#     "django-db"  # Используем базу данных Django для хранения результатов задач
# )
# CELERY_RESULT_EXPIRES = 60 * 60 * 24  # 24 часа
# CELERY_RESULT_DB_TABLE_NAME = "celery_results"
# CELERY_TIMEZONE = "Europe/Moscow"

# celery -A task worker --loglevel=INFO
# CELERY_BROKER_URL = 'redis://127.0.0.1:6379/0'
# CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND")
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"
CELERY_TIMEZONE = "Europe/Moscow"
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
# если планировщик запущен, добавить в .env INCLUDE_CELERY = True
# INCLUDE_CELERY = os.getenv("INCLUDE_CELERY", False)
