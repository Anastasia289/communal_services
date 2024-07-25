from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer, ValidationError
from services.models import (
    Apartment,
    House,
    Rent,
    Tariff,
    WaterMeter,
    WaterMeterData,
)
from users.models import CustomUser


class CustomUserSerializer(UserSerializer):
    """Сериализатор для управления пользователями."""

    class Meta:
        model = CustomUser
        fields = (
            "id",
            "username",
            "email",
            "password",
        )


class CustomUserCreateSerializer(UserCreateSerializer):
    """Сериализатор для создания пользователя."""

    class Meta:
        model = CustomUser
        fields = (
            "id",
            "username",
            "email",
            "password",
        )


class HouseGetSerializer(ModelSerializer):
    """Сериализатор для получения полной информации о доме."""

    apartment = SerializerMethodField()

    class Meta:
        model = House
        fields = ("id", "name", "adress", "apartment")

    def get_apartment(self, obj):
        apartment = Apartment.objects.filter(house=obj).all()
        return ApartmentGetSerializer(apartment, many=True).data


class ApartmentGetSerializer(ModelSerializer):
    """Сериализатор для получения полной информации о квартире."""

    watermeter = SerializerMethodField()

    class Meta:
        model = Apartment
        fields = ("id", "number", "house", "area", "watermeter")

    def get_watermeter(self, obj):
        watermeter = WaterMeter.objects.filter(apartment=obj).all()
        return WaterMeterGetSerializer(watermeter, many=True).data


class WaterMeterGetSerializer(ModelSerializer):
    """Сериализатор для получения полной информации о счетчике."""

    watermeterdata = SerializerMethodField()

    class Meta:
        model = WaterMeter
        fields = (
            "id",
            "number",
            "valid_till",
            "apartment",
            "watermeterdata",
        )

    def get_watermeterdata(self, obj):
        watermeterdata = WaterMeterData.objects.filter(water_meter=obj).all()
        return WaterMeterDataSerializer(watermeterdata, many=True).data


class WaterMeterDataSerializer(ModelSerializer):
    """Показания счетчиков."""

    class Meta:
        model = WaterMeterData
        fields = (
            "id",
            "water_meter",
            "meter_readings",
            "date",
            "year",
            "month",
        )

    def validate(self, data):
        water_meter = data["water_meter"]
        year = data["year"]
        month = data["month"]
        if WaterMeterData.objects.filter(
            water_meter=water_meter, year=year, month=month
        ).exists():
            raise ValidationError("За этот месяц показания уже поданы")
        return data


class TariffSerializer(ModelSerializer):
    """Тарифы."""

    class Meta:
        model = Tariff
        fields = ("id", "name", "description", "average_readings", "price")


class RentSerializer(ModelSerializer):
    """Квартплата."""

    class Meta:
        model = Rent
        fields = (
            "id",
            "apartment",
            "water_price",
            "property_price",
            "year",
            "month",
            "date",
        )

    def validate(self, data):
        apartment = data["apartment"]
        year = data["year"]
        month = data["month"]
        if Rent.objects.filter(
            apartment=apartment, year=year, month=month
        ).exists():
            raise ValidationError("За этот месяц квартплата уже начислена")
        return data
