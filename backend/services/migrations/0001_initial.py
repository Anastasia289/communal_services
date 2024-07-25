# Generated by Django 4.2.9 on 2024-07-24 16:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField(verbose_name='Номер квартиры')),
                ('area', models.PositiveSmallIntegerField(verbose_name='Площадь квартиры')),
            ],
            options={
                'verbose_name': 'Квартира',
                'verbose_name_plural': 'Квартиры',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='название/номер дома')),
                ('adress', models.CharField(max_length=150, verbose_name='адрес дома')),
            ],
            options={
                'verbose_name': 'Дом',
                'verbose_name_plural': 'Дома',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Tariff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название тарифа')),
                ('description', models.CharField(max_length=150, verbose_name='Описание тарифа')),
                ('average_readings', models.PositiveSmallIntegerField(verbose_name='Cреднее показание на случай если счетчик просрочен')),
                ('price', models.PositiveSmallIntegerField(verbose_name='Цена за единицу')),
            ],
            options={
                'verbose_name': 'Тариф',
                'verbose_name_plural': 'Тарифы',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='WaterMeter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField(verbose_name='Номер счетчика')),
                ('valid_till', models.DateField(verbose_name='Когда заканчивается срок службы')),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apartment', to='services.apartment', verbose_name='квартира')),
            ],
            options={
                'verbose_name': 'Счетчик',
                'verbose_name_plural': 'Счетчики',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='WaterMeterData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meter_readings', models.PositiveSmallIntegerField(verbose_name='Показания счетчика')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата снятия показаний')),
                ('year', models.PositiveSmallIntegerField(verbose_name='Год')),
                ('month', models.PositiveSmallIntegerField(verbose_name='Месяц')),
                ('water_meter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='water_meter', to='services.watermeter', verbose_name='счетчик')),
            ],
            options={
                'verbose_name': 'Показания счетчика',
                'verbose_name_plural': 'Показания счетчиков',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('water_price', models.FloatField(verbose_name='Цена за воду')),
                ('property_price', models.FloatField(verbose_name='Цена за содержание общего имущества')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата показаний')),
                ('year', models.PositiveSmallIntegerField(verbose_name='Год')),
                ('month', models.PositiveSmallIntegerField(verbose_name='Месяц')),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rent', to='services.apartment', verbose_name='квартплата')),
            ],
            options={
                'verbose_name': 'Квартплата',
                'verbose_name_plural': 'Квартплаты',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='apartment',
            name='house',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='house', to='services.house', verbose_name='дом'),
        ),
    ]
