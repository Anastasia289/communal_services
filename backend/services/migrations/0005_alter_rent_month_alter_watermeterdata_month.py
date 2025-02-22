# Generated by Django 4.2.9 on 2024-07-25 18:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_alter_rent_year_alter_watermeterdata_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent',
            name='month',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(12, message='В году их только 12')], verbose_name='Месяц'),
        ),
        migrations.AlterField(
            model_name='watermeterdata',
            name='month',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(12, message='В году их только 12')], verbose_name='Месяц'),
        ),
    ]
