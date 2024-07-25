from django.db import migrations


def add_data(apps, schema_editor):
    WaterMeterData = apps.get_model("services", "WaterMeterData")

    data = [
        {'water_meter_id': '1', 'meter_readings': 1, 'year': 2019, 'month': 1},
        {'water_meter_id': '1', 'meter_readings': 1, 'year': 2023, 'month': 1},
        {'water_meter_id': '1', 'meter_readings': 3, 'year': 2023, 'month': 2},
        {'water_meter_id': '1', 'meter_readings': 5, 'year': 2023, 'month': 3},
        {'water_meter_id': '1', 'meter_readings': 6, 'year': 2023, 'month': 4},
        {'water_meter_id': '1', 'meter_readings': 7, 'year': 2023, 'month': 5},
        {'water_meter_id': '1', 'meter_readings': 12, 'year': 2023, 'month': 6},
        {'water_meter_id': '1', 'meter_readings': 14, 'year': 2023, 'month': 7},
        {'water_meter_id': '1', 'meter_readings': 17, 'year': 2023, 'month': 8},
        {'water_meter_id': '1', 'meter_readings': 21, 'year': 2023, 'month': 9},
        {'water_meter_id': '1', 'meter_readings': 24, 'year': 2023, 'month': 10},
        {'water_meter_id': '1', 'meter_readings': 36, 'year': 2023, 'month': 11},
        {'water_meter_id': '1', 'meter_readings': 39, 'year': 2023, 'month': 12},
        {'water_meter_id': '1', 'meter_readings': 41, 'year': 2024, 'month': 1},
        {'water_meter_id': '1', 'meter_readings': 43, 'year': 2024, 'month': 2},
        {'water_meter_id': '1', 'meter_readings': 45, 'year': 2024, 'month': 3},
        {'water_meter_id': '1', 'meter_readings': 47, 'year': 2024, 'month': 4},
        {'water_meter_id': '1', 'meter_readings': 48, 'year': 2024, 'month': 5},
        {'water_meter_id': '1', 'meter_readings': 49, 'year': 2024, 'month': 6},
        {'water_meter_id': '1', 'meter_readings': 50, 'year': 2024, 'month': 7},
        
        {'water_meter_id': '2', 'meter_readings': 4, 'year': 2023, 'month': 1},
        {'water_meter_id': '2', 'meter_readings': 7, 'year': 2023, 'month': 2},
        {'water_meter_id': '2', 'meter_readings': 8, 'year': 2023, 'month': 3},
        {'water_meter_id': '2', 'meter_readings': 12, 'year': 2023, 'month': 4},
        {'water_meter_id': '2', 'meter_readings': 14, 'year': 2023, 'month': 5},
        {'water_meter_id': '2', 'meter_readings': 16, 'year': 2023, 'month': 6},
        {'water_meter_id': '2', 'meter_readings': 16, 'year': 2023, 'month': 7},
        {'water_meter_id': '2', 'meter_readings': 17, 'year': 2023, 'month': 8},
        {'water_meter_id': '2', 'meter_readings': 24, 'year': 2023, 'month': 9},
        {'water_meter_id': '2', 'meter_readings': 25, 'year': 2023, 'month': 10},
        {'water_meter_id': '2', 'meter_readings': 29, 'year': 2023, 'month': 11},
        {'water_meter_id': '2', 'meter_readings': 31, 'year': 2023, 'month': 12},
        {'water_meter_id': '2', 'meter_readings': 33, 'year': 2024, 'month': 1},
        {'water_meter_id': '2', 'meter_readings': 36, 'year': 2024, 'month': 2},
        {'water_meter_id': '2', 'meter_readings': 38, 'year': 2024, 'month': 3},
        {'water_meter_id': '2', 'meter_readings': 43, 'year': 2024, 'month': 4},
        {'water_meter_id': '2', 'meter_readings': 48, 'year': 2024, 'month': 5},
        {'water_meter_id': '2', 'meter_readings': 54, 'year': 2024, 'month': 6},
        {'water_meter_id': '2', 'meter_readings': 59, 'year': 2024, 'month': 7},
        
        {'water_meter_id': '3', 'meter_readings': 11, 'year': 2023, 'month': 1},
        {'water_meter_id': '3', 'meter_readings': 32, 'year': 2023, 'month': 2},
        {'water_meter_id': '3', 'meter_readings': 37, 'year': 2023, 'month': 3},
        {'water_meter_id': '3', 'meter_readings': 46, 'year': 2023, 'month': 4},
        {'water_meter_id': '3', 'meter_readings': 52, 'year': 2023, 'month': 5},
        {'water_meter_id': '3', 'meter_readings': 63, 'year': 2023, 'month': 6},
        {'water_meter_id': '3', 'meter_readings': 68, 'year': 2023, 'month': 7},
        {'water_meter_id': '3', 'meter_readings': 74, 'year': 2023, 'month': 8},
        {'water_meter_id': '3', 'meter_readings': 79, 'year': 2023, 'month': 9},
        {'water_meter_id': '3', 'meter_readings': 82, 'year': 2023, 'month': 10},
        {'water_meter_id': '3', 'meter_readings': 88, 'year': 2023, 'month': 11},
        {'water_meter_id': '3', 'meter_readings': 90, 'year': 2023, 'month': 12},
        {'water_meter_id': '3', 'meter_readings': 91, 'year': 2024, 'month': 1},
        {'water_meter_id': '3', 'meter_readings': 97, 'year': 2024, 'month': 2},
        {'water_meter_id': '3', 'meter_readings': 101, 'year': 2024, 'month': 3},
        {'water_meter_id': '3', 'meter_readings': 108, 'year': 2024, 'month': 4},
        {'water_meter_id': '3', 'meter_readings': 110, 'year': 2024, 'month': 5},
        {'water_meter_id': '3', 'meter_readings': 115, 'year': 2024, 'month': 6},
        {'water_meter_id': '3', 'meter_readings': 124, 'year': 2024, 'month': 7},
        
        {'water_meter_id': '4', 'meter_readings': 1, 'year': 2023, 'month': 1},
        {'water_meter_id': '4', 'meter_readings': 3, 'year': 2023, 'month': 2},
        {'water_meter_id': '4', 'meter_readings': 5, 'year': 2023, 'month': 3},
        {'water_meter_id': '4', 'meter_readings': 6, 'year': 2023, 'month': 4},
        {'water_meter_id': '4', 'meter_readings': 7, 'year': 2023, 'month': 5},
        {'water_meter_id': '4', 'meter_readings': 9, 'year': 2023, 'month': 6},
        {'water_meter_id': '4', 'meter_readings': 9, 'year': 2023, 'month': 7},
        {'water_meter_id': '4', 'meter_readings': 9, 'year': 2023, 'month': 8},
        {'water_meter_id': '4', 'meter_readings': 12, 'year': 2023, 'month': 9},
        {'water_meter_id': '4', 'meter_readings': 20, 'year': 2023, 'month': 10},
        {'water_meter_id': '4', 'meter_readings': 22, 'year': 2023, 'month': 11},
        {'water_meter_id': '4', 'meter_readings': 23, 'year': 2023, 'month': 12},
        {'water_meter_id': '4', 'meter_readings': 26, 'year': 2024, 'month': 1},
        {'water_meter_id': '4', 'meter_readings': 30, 'year': 2024, 'month': 2},
        {'water_meter_id': '4', 'meter_readings': 33, 'year': 2024, 'month': 3},
        {'water_meter_id': '4', 'meter_readings': 36, 'year': 2024, 'month': 4},
        {'water_meter_id': '4', 'meter_readings': 39, 'year': 2024, 'month': 5},
        {'water_meter_id': '4', 'meter_readings': 41, 'year': 2024, 'month': 6},
        {'water_meter_id': '4', 'meter_readings': 44, 'year': 2024, 'month': 7},
        
        {'water_meter_id': '5', 'meter_readings': 6, 'year': 2023, 'month': 1},
        {'water_meter_id': '5', 'meter_readings': 12, 'year': 2023, 'month': 2},
        {'water_meter_id': '5', 'meter_readings': 19, 'year': 2023, 'month': 3},
        {'water_meter_id': '5', 'meter_readings': 23, 'year': 2023, 'month': 4},
        {'water_meter_id': '5', 'meter_readings': 26, 'year': 2023, 'month': 5},
        {'water_meter_id': '5', 'meter_readings': 31, 'year': 2023, 'month': 6},
        {'water_meter_id': '5', 'meter_readings': 33, 'year': 2023, 'month': 7},
        {'water_meter_id': '5', 'meter_readings': 38, 'year': 2023, 'month': 8},
        {'water_meter_id': '5', 'meter_readings': 41, 'year': 2023, 'month': 9},
        {'water_meter_id': '5', 'meter_readings': 47, 'year': 2023, 'month': 10},
        {'water_meter_id': '5', 'meter_readings': 55, 'year': 2023, 'month': 11},
        {'water_meter_id': '5', 'meter_readings': 59, 'year': 2023, 'month': 12},
        {'water_meter_id': '5', 'meter_readings': 61, 'year': 2024, 'month': 1},
        {'water_meter_id': '5', 'meter_readings': 65, 'year': 2024, 'month': 2},
        {'water_meter_id': '5', 'meter_readings': 70, 'year': 2024, 'month': 3},
        {'water_meter_id': '5', 'meter_readings': 77, 'year': 2024, 'month': 4},
        {'water_meter_id': '5', 'meter_readings': 78, 'year': 2024, 'month': 5},
        {'water_meter_id': '5', 'meter_readings': 81, 'year': 2024, 'month': 6},
        {'water_meter_id': '5', 'meter_readings': 82, 'year': 2024, 'month': 7},
        
        {'water_meter_id': '6', 'meter_readings': 51, 'year': 2023, 'month': 1},
        {'water_meter_id': '6', 'meter_readings': 56, 'year': 2023, 'month': 2},
        {'water_meter_id': '6', 'meter_readings': 58, 'year': 2023, 'month': 3},
        {'water_meter_id': '6', 'meter_readings': 62, 'year': 2023, 'month': 4},
        {'water_meter_id': '6', 'meter_readings': 67, 'year': 2023, 'month': 5},
        {'water_meter_id': '6', 'meter_readings': 69, 'year': 2023, 'month': 6},
        {'water_meter_id': '6', 'meter_readings': 73, 'year': 2023, 'month': 7},
        {'water_meter_id': '6', 'meter_readings': 77, 'year': 2023, 'month': 8},
        {'water_meter_id': '6', 'meter_readings': 84, 'year': 2023, 'month': 9},
        {'water_meter_id': '6', 'meter_readings': 89, 'year': 2023, 'month': 10},
        {'water_meter_id': '6', 'meter_readings': 99, 'year': 2023, 'month': 11},
        {'water_meter_id': '6', 'meter_readings': 110, 'year': 2023, 'month': 12},
        {'water_meter_id': '6', 'meter_readings': 112, 'year': 2024, 'month': 1},
        {'water_meter_id': '6', 'meter_readings': 119, 'year': 2024, 'month': 2},
        {'water_meter_id': '6', 'meter_readings': 124, 'year': 2024, 'month': 3},
        {'water_meter_id': '6', 'meter_readings': 129, 'year': 2024, 'month': 4},
        {'water_meter_id': '6', 'meter_readings': 132, 'year': 2024, 'month': 5},
        {'water_meter_id': '6', 'meter_readings': 139, 'year': 2024, 'month': 6},
        {'water_meter_id': '6', 'meter_readings': 144, 'year': 2024, 'month': 7},
        
        {'water_meter_id': '7', 'meter_readings': 1, 'year': 2023, 'month': 1},
        {'water_meter_id': '7', 'meter_readings': 3, 'year': 2023, 'month': 2},
        {'water_meter_id': '7', 'meter_readings': 5, 'year': 2023, 'month': 3},
        {'water_meter_id': '7', 'meter_readings': 7, 'year': 2023, 'month': 4},
        {'water_meter_id': '7', 'meter_readings': 9, 'year': 2023, 'month': 5},
        {'water_meter_id': '7', 'meter_readings': 11, 'year': 2023, 'month': 6},
        {'water_meter_id': '7', 'meter_readings': 13, 'year': 2023, 'month': 7},
        {'water_meter_id': '7', 'meter_readings': 15, 'year': 2023, 'month': 8},
        {'water_meter_id': '7', 'meter_readings': 17, 'year': 2023, 'month': 9},
        {'water_meter_id': '7', 'meter_readings': 19, 'year': 2023, 'month': 10},
        {'water_meter_id': '7', 'meter_readings': 21, 'year': 2023, 'month': 11},
        {'water_meter_id': '7', 'meter_readings': 23, 'year': 2023, 'month': 12},
        {'water_meter_id': '7', 'meter_readings': 25, 'year': 2024, 'month': 1},
        {'water_meter_id': '7', 'meter_readings': 27, 'year': 2024, 'month': 2},
        {'water_meter_id': '7', 'meter_readings': 29, 'year': 2024, 'month': 3},
        {'water_meter_id': '7', 'meter_readings': 31, 'year': 2024, 'month': 4},
        {'water_meter_id': '7', 'meter_readings': 33, 'year': 2024, 'month': 5},
        {'water_meter_id': '7', 'meter_readings': 35, 'year': 2024, 'month': 6},
        {'water_meter_id': '7', 'meter_readings': 37, 'year': 2024, 'month': 7},
        
        {'water_meter_id': '8', 'meter_readings': 1, 'year': 2023, 'month': 1},
        {'water_meter_id': '8', 'meter_readings': 6, 'year': 2023, 'month': 2},
        {'water_meter_id': '8', 'meter_readings': 11, 'year': 2023, 'month': 3},
        {'water_meter_id': '8', 'meter_readings': 17, 'year': 2023, 'month': 4},
        {'water_meter_id': '8', 'meter_readings': 24, 'year': 2023, 'month': 5},
        {'water_meter_id': '8', 'meter_readings': 30, 'year': 2023, 'month': 6},
        {'water_meter_id': '8', 'meter_readings': 36, 'year': 2023, 'month': 7},
        {'water_meter_id': '8', 'meter_readings': 42, 'year': 2023, 'month': 8},
        {'water_meter_id': '8', 'meter_readings': 49, 'year': 2023, 'month': 9},
        {'water_meter_id': '8', 'meter_readings': 55, 'year': 2023, 'month': 10},
        {'water_meter_id': '8', 'meter_readings': 62, 'year': 2023, 'month': 11},
        {'water_meter_id': '8', 'meter_readings': 69, 'year': 2023, 'month': 12},
        {'water_meter_id': '8', 'meter_readings': 73, 'year': 2024, 'month': 1},
        {'water_meter_id': '8', 'meter_readings': 80, 'year': 2024, 'month': 2},
        {'water_meter_id': '8', 'meter_readings': 85, 'year': 2024, 'month': 3},
        {'water_meter_id': '8', 'meter_readings': 91, 'year': 2024, 'month': 4},
        {'water_meter_id': '8', 'meter_readings': 98, 'year': 2024, 'month': 5},
        {'water_meter_id': '8', 'meter_readings': 104, 'year': 2024, 'month': 6},
        {'water_meter_id': '8', 'meter_readings': 111, 'year': 2024, 'month': 7},
        
        {'water_meter_id': '9', 'meter_readings': 31, 'year': 2023, 'month': 1},
        {'water_meter_id': '9', 'meter_readings': 39, 'year': 2023, 'month': 2},
        {'water_meter_id': '9', 'meter_readings': 45, 'year': 2023, 'month': 3},
        {'water_meter_id': '9', 'meter_readings': 58, 'year': 2023, 'month': 4},
        {'water_meter_id': '9', 'meter_readings': 81, 'year': 2023, 'month': 5},
        {'water_meter_id': '9', 'meter_readings': 94, 'year': 2023, 'month': 6},
        {'water_meter_id': '9', 'meter_readings': 102, 'year': 2023, 'month': 7},
        {'water_meter_id': '9', 'meter_readings': 116, 'year': 2023, 'month': 8},
        {'water_meter_id': '9', 'meter_readings': 131, 'year': 2023, 'month': 9},
        {'water_meter_id': '9', 'meter_readings': 143, 'year': 2023, 'month': 10},
        {'water_meter_id': '9', 'meter_readings': 156, 'year': 2023, 'month': 11},
        {'water_meter_id': '9', 'meter_readings': 168, 'year': 2023, 'month': 12},
        {'water_meter_id': '9', 'meter_readings': 182, 'year': 2024, 'month': 1},
        {'water_meter_id': '9', 'meter_readings': 193, 'year': 2024, 'month': 2},
        {'water_meter_id': '9', 'meter_readings': 204, 'year': 2024, 'month': 3},
        {'water_meter_id': '9', 'meter_readings': 213, 'year': 2024, 'month': 4},
        {'water_meter_id': '9', 'meter_readings': 229, 'year': 2024, 'month': 5},
        {'water_meter_id': '9', 'meter_readings': 237, 'year': 2024, 'month': 6},
        {'water_meter_id': '9', 'meter_readings': 245, 'year': 2024, 'month': 7},
        
        {'water_meter_id': '10', 'meter_readings': 33, 'year': 2023, 'month': 1},
        {'water_meter_id': '10', 'meter_readings': 44, 'year': 2023, 'month': 2},
        {'water_meter_id': '10', 'meter_readings': 44, 'year': 2023, 'month': 3},
        {'water_meter_id': '10', 'meter_readings': 55, 'year': 2023, 'month': 4},
        {'water_meter_id': '10', 'meter_readings': 66, 'year': 2023, 'month': 5},
        {'water_meter_id': '10', 'meter_readings': 77, 'year': 2023, 'month': 6},
        {'water_meter_id': '10', 'meter_readings': 88, 'year': 2023, 'month': 7},
        {'water_meter_id': '10', 'meter_readings': 99, 'year': 2023, 'month': 8},
        {'water_meter_id': '10', 'meter_readings': 110, 'year': 2023, 'month': 9},
        {'water_meter_id': '10', 'meter_readings': 123, 'year': 2023, 'month': 10},
        {'water_meter_id': '10', 'meter_readings': 134, 'year': 2023, 'month': 11},
        {'water_meter_id': '10', 'meter_readings': 145, 'year': 2023, 'month': 12},
        {'water_meter_id': '10', 'meter_readings': 156, 'year': 2024, 'month': 1},
        {'water_meter_id': '10', 'meter_readings': 165, 'year': 2024, 'month': 2},
        {'water_meter_id': '10', 'meter_readings': 175, 'year': 2024, 'month': 3},
        {'water_meter_id': '10', 'meter_readings': 187, 'year': 2024, 'month': 4},
        {'water_meter_id': '10', 'meter_readings': 198, 'year': 2024, 'month': 5},
        {'water_meter_id': '10', 'meter_readings': 202, 'year': 2024, 'month': 6},
        {'water_meter_id': '10', 'meter_readings': 210, 'year': 2024, 'month': 7},

    ]
    for row in data:
        WaterMeterData.objects.update_or_create(**row)


class Migration(migrations.Migration):
    dependencies = [
        ('services', '0002_add_houses,apart'),
    ]

    operations = [
        migrations.RunPython(add_data),
    ]