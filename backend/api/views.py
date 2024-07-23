# import requests
from api.serializers import (
    ApartmentGetSerializer,
    HouseGetSerializer,
    RentSerializer,
    TariffSerializer,
    WaterMeterDataSerializer,
    WaterMeterGetSerializer,
)

# from django.shortcuts import get_object_or_404, render
# from django_filters.rest_framework import DjangoFilterBackend
from djoser.views import UserViewSet
from rest_framework import viewsets  # status,

# from rest_framework.filters import OrderingFilter, SearchFilter
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
from services.models import (
    Apartment,
    House,
    Rent,
    Tariff,
    WaterMeter,
    WaterMeterData,
)
from users.models import CustomUser

from .serializers import CustomUserSerializer


class CustomUserViewSet(UserViewSet):
    """Вьюсет для пользователей."""

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    http_method_names = [
        "get",
        "post",
    ]


class HouseViewSet(viewsets.ModelViewSet):
    """House."""

    queryset = House.objects.all()
    serializer_class = HouseGetSerializer


class ApartmentViewSet(viewsets.ModelViewSet):
    """Apartment."""

    queryset = Apartment.objects.all()
    serializer_class = ApartmentGetSerializer


class WaterMeterViewSet(viewsets.ModelViewSet):
    """WaterMeter."""

    queryset = WaterMeter.objects.all()
    serializer_class = WaterMeterGetSerializer


class WaterMeterDataViewSet(viewsets.ModelViewSet):
    """WaterMeterData."""

    queryset = WaterMeterData.objects.all()
    serializer_class = WaterMeterDataSerializer


class TariffViewSet(viewsets.ModelViewSet):
    """Tariff."""

    queryset = Tariff.objects.all()
    serializer_class = TariffSerializer


class RentViewSet(viewsets.ModelViewSet):
    """Rent."""

    queryset = Rent.objects.all()
    serializer_class = RentSerializer
