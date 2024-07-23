# import requests
# from django.shortcuts import get_object_or_404, render
# from django_filters.rest_framework import DjangoFilterBackend
from djoser.views import UserViewSet
from users.models import CustomUser

from .serializers import CustomUserSerializer

# from rest_framework import status, viewsets
# from rest_framework.filters import OrderingFilter, SearchFilter
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response


class CustomUserViewSet(UserViewSet):
    """Вьюсет для пользователей."""

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    http_method_names = [
        "get",
        "post",
    ]
