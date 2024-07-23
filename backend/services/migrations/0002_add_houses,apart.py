from django.db import migrations

def add_data(apps, schema_editor):
    House = apps.get_model("services", "House")

    House.objects.get_or_create(
        name='1',
        adress='Где-то не очень далеко'
    )

    House.objects.get_or_create(
        name='2',
        adress='Где-то чуть ближе'
    )

    Apartment = apps.get_model("services", "Apartment")

    Apartment.objects.get_or_create(
        house_id='1',
        number='1',
        area=35
    )
    
    Apartment.objects.get_or_create(
        house_id='1',
        number='2',
        area=67
    )
    Apartment.objects.get_or_create(
        house_id='1',
        number='3',
        area=84
    )
    Apartment.objects.get_or_create(
        house_id='1',
        number='4',
        area=72
    )
    Apartment.objects.get_or_create(
        house_id='2',
        number='1',
        area=43
    )
    Apartment.objects.get_or_create(
        house_id='2',
        number='2',
        area=56
    )
    
    WaterMeter = apps.get_model("services", "WaterMeter")
    
    WaterMeter.objects.get_or_create(
        number='12345',
        valid_till='2025-12-23',
        apartment_id=1
    )
    
    WaterMeter.objects.get_or_create(
        number='2345',
        valid_till='2025-11-24',
        apartment_id=1
    )
    
    WaterMeter.objects.get_or_create(
        number='65456',
        valid_till='2026-12-23',
        apartment_id=1
    )
    
    WaterMeter.objects.get_or_create(
        number='15567',
        valid_till='2027-12-23',
        apartment_id=2
    )
    
    WaterMeter.objects.get_or_create(
        number='12654',
        valid_till='2022-12-23',
        apartment_id=2
    )
    
    WaterMeter.objects.get_or_create(
        number='127654',
        valid_till='2025-12-23',
        apartment_id=3
    )
    
    WaterMeter.objects.get_or_create(
        number='1285948',
        valid_till='2028-12-23',
        apartment_id=4
    )
    
    WaterMeter.objects.get_or_create(
        number='1298785',
        valid_till='2024-11-23',
        apartment_id=5
    )
    
    WaterMeter.objects.get_or_create(
        number='129734',
        valid_till='2025-12-23',
        apartment_id=5
    )
    
    WaterMeter.objects.get_or_create(
        number='1236324',
        valid_till='2029-12-23',
        apartment_id=6
    )
    
    Tariff = apps.get_model("services", "Tariff")

    Tariff.objects.get_or_create(
        name='Тариф за воду',
        description='Это важно',
        average_readings=4,
        price=274
    )
    
    Tariff.objects.get_or_create(
        name='Тариф за содержание общего имущества',
        description='Это не любят',
        average_readings=0,
        price=100
    )


class Migration(migrations.Migration):
    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_data),
    ]