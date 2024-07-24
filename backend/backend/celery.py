import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

sched = Celery("backend")

sched.config_from_object("django.conf:settings", namespace="CELERY")

sched.autodiscover_tasks()
