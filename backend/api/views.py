from djoser.views import UserViewSet
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from services.models import (
    Apartment,
    House,
    Rent,
    Tariff,
    WaterMeter,
    WaterMeterData,
)
from users.models import CustomUser

from .serializers import (
    ApartmentGetSerializer,
    CustomUserSerializer,
    HouseGetSerializer,
    RentSerializer,
    TariffSerializer,
    WaterMeterDataSerializer,
    WaterMeterGetSerializer,
)
from .tasks import get_rent


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

    @action(
        detail=False,
        # detail=True,
        methods=["post"],
        url_path="get_rent_per_month",
    )
    def create_rent_per_month(self, request, *args):
        """Рассчет квартплаты по дому за указанный месяц."""
        month = self.request.data.get("month")
        year = self.request.data.get("year")
        house_id = self.request.data.get("house_id")
        get_rent.delay(
            house_id,
            year,
            month,
        )
        return Response(
            "Выполняется расчет квартплаты", status=status.HTTP_204_NO_CONTENT
        )
