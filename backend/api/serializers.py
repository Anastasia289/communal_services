from djoser.serializers import UserCreateSerializer, UserSerializer

# from rest_framework.fields import SerializerMethodField
from users.models import CustomUser

# from rest_framework import serializers


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
