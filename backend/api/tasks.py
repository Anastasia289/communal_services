from celery import shared_task
from services.models import Apartment, Tariff, WaterMeter, WaterMeterData

from .serializers import RentSerializer


@shared_task
def get_used_water(apartment, year, month, tariff_average_readings):
    """Получаем количество потраченной воды за месяц со всех счетчиков."""
    result = 0
    watermeters = WaterMeter.objects.filter(apartment=apartment.id)
    for watermeter in watermeters:
        current = WaterMeterData.objects.get(
            water_meter=watermeter.id, year=year, month=month
        )
        if not current:
            print("нет текущих показаний")
            return 2
        if month == 1:
            previous = WaterMeterData.objects.get(
                id=watermeter.id, year=int(year) - 1, month=12
            )
        previous = WaterMeterData.objects.get(
            water_meter=watermeter.id, year=year, month=int(month) - 1
        )
        if not previous:
            print("нет предыдущих показаний")
            return 3
        res = current.meter_readings - previous.meter_readings
        result += res
    return result


@shared_task
def get_rent(
    house_id,
    year,
    month,
):
    """Рассчет квартплаты за месяц для всех квартир в доме."""
    water_tariff = Tariff.objects.get(id=1)
    common_property_tariff = Tariff.objects.get(id=2)
    apartments = Apartment.objects.filter(house=house_id)
    property_price = common_property_tariff.price
    for apartment in apartments:
        used_water = get_used_water(
            apartment, year, month, common_property_tariff.average_readings
        )

        serializer = RentSerializer(
            data={
                "apartment": apartment.id,
                "water_price": used_water * water_tariff.price,
                "property_price": property_price * apartment.area,
                "year": int(year),
                "month": int(month),
            },
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
