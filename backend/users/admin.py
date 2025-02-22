from django.contrib import admin

from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "password")
    search_fields = ("username", "email")
    empty_value_display = "-пусто-"


admin.site.register(CustomUser, CustomUserAdmin)
