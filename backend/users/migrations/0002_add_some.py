# Generated by Django 4.2.9 on 2024-03-23 19:24
from datetime import datetime

from django.contrib.auth.hashers import make_password
from django.db import migrations
from django.utils import timezone


def add_users(apps, schema_editor):
    CustomUser = apps.get_model("users", "CustomUser")

    tz = timezone.get_current_timezone()
    now_datetime = datetime.now().replace(tzinfo=tz)

    CustomUser.objects.get_or_create(
        username='admin',
        password=make_password('admin'),
        email='admin@ad.ru',
        is_superuser=True,
        is_staff=True
    )

    CustomUser.objects.get_or_create(
        username='vasya',
        password=make_password('zxc102938'),
        email='vasya@admin.ru',
        is_superuser=False,
        is_staff=True
    )
    CustomUser.objects.get_or_create(
        username='joe',
        password=make_password('mko091122'),
        email='joe@joe.ru',
        is_superuser=False,
        is_staff=True
    )

class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_users),
    ]
