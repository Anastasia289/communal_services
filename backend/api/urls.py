from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    ApartmentViewSet,
    CustomUserViewSet,
    HouseViewSet,
    RentViewSet,
    TariffViewSet,
    WaterMeterDataViewSet,
    WaterMeterViewSet,
)

app_name = "api"
router_v1 = DefaultRouter()

router_v1.register("users", CustomUserViewSet, basename="users")
router_v1.register("house", HouseViewSet, basename="house")
router_v1.register("apartment", ApartmentViewSet, basename="apartment")
router_v1.register("watermeter", WaterMeterViewSet, basename="watermeter")
router_v1.register(
    "watermeterdata", WaterMeterDataViewSet, basename="watermeterdata"
)
router_v1.register("tariff", TariffViewSet, basename="tariff")
router_v1.register("rent", RentViewSet, basename="rent")


urlpatterns = [
    path("v1/", include(router_v1.urls)),
    path("auth/", include("djoser.urls.authtoken")),
]
