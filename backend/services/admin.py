from django.contrib import admin
from services import models


class HouseAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "adress",
    )
    empty_value_display = "-пусто-"


class ApartmentAdmin(admin.ModelAdmin):
    list_display = ("id", "number", "house", "area")
    empty_value_display = "-пусто-"


class WaterMeterAdmin(admin.ModelAdmin):
    list_display = ("id", "number", "valid_till", "apartment")
    empty_value_display = "-пусто-"


class WaterMeterDataAdmin(admin.ModelAdmin):
    list_display = ("id", "water_meter", "meter_readings", "date")
    empty_value_display = "-пусто-"


class TariffAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "average_readings", "price")
    empty_value_display = "-пусто-"


class RentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "apartment",
        "water_price",
        "property_price",
        "date",
    )
    empty_value_display = "-пусто-"


admin.site.register(models.House, HouseAdmin)
admin.site.register(models.Apartment, ApartmentAdmin)
admin.site.register(models.WaterMeter, WaterMeterAdmin)
admin.site.register(models.WaterMeterData, WaterMeterDataAdmin)
admin.site.register(models.Tariff, TariffAdmin)
admin.site.register(models.Rent, RentAdmin)
