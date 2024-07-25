from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from backend.constants import MAX_CHAR_LENGTH, MAX_MONTH, MAX_YEAR, MIN_YEAR

User = get_user_model()


class DateModel(models.Model):
    """Абстрактная модель счетчиков."""

    date = models.DateField(
        auto_now_add=True,
        verbose_name="Дата показаний",
    )
    year = models.PositiveSmallIntegerField(
        "Год",
        validators=[
            MinValueValidator(MIN_YEAR, message="Тогда мы еще не работали"),
            MaxValueValidator(MAX_YEAR, message="Слишком далеко в будущее"),
        ],
    )
    month = models.PositiveSmallIntegerField(
        "Месяц",
        validators=[
            MaxValueValidator(MAX_MONTH, message="В году их только 12")
        ],
    )

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.month} - {self.year} - {self.date} "


class House(models.Model):
    """Дом. В доме может быть много квартир."""

    name = models.CharField("название/номер дома", max_length=MAX_CHAR_LENGTH)
    adress = models.CharField("адрес дома", max_length=MAX_CHAR_LENGTH)

    class Meta:
        verbose_name = "Дом"
        verbose_name_plural = "Дома"
        ordering = ["id"]

    def __str__(self):
        return f"{self.name} - {self.adress}"


class Apartment(models.Model):
    """Квартира."""

    house = models.ForeignKey(
        House,
        on_delete=models.CASCADE,
        related_name="house",
        verbose_name="дом",
    )
    number = models.PositiveSmallIntegerField("Номер квартиры")
    area = models.PositiveSmallIntegerField("Площадь квартиры")

    class Meta:
        verbose_name = "Квартира"
        verbose_name_plural = "Квартиры"
        ordering = ["id"]

    def __str__(self):
        return f"Дом {self.house.name} - квартира №{self.number}"


class WaterMeter(models.Model):
    """Счетчик воды."""

    number = models.PositiveSmallIntegerField("Номер счетчика")
    valid_till = models.DateField("Когда заканчивается срок службы")
    apartment = models.ForeignKey(
        Apartment,
        on_delete=models.CASCADE,
        related_name="apartment",
        verbose_name="квартира",
    )

    class Meta:
        verbose_name = "Счетчик"
        verbose_name_plural = "Счетчики"
        ordering = ["id"]

    def __str__(self):
        return f"Счетчик {self.number} в квартире {self.apartment}"


class WaterMeterData(DateModel):
    """Показания счетчика за несколько месяцев."""

    water_meter = models.ForeignKey(
        WaterMeter,
        on_delete=models.CASCADE,
        related_name="water_meter",
        verbose_name="счетчик",
    )
    meter_readings = models.PositiveSmallIntegerField("Показания счетчика")

    class Meta:
        verbose_name = "Показания счетчика"
        verbose_name_plural = "Показания счетчиков"
        ordering = ["id"]

    def __str__(self):
        return f"{self.water_meter} - {self.meter_readings}"


class Tariff(models.Model):
    """Тариф. Цена услуги или ресурса."""

    name = models.CharField("Название тарифа", max_length=MAX_CHAR_LENGTH)
    description = models.CharField(
        "Описание тарифа", max_length=MAX_CHAR_LENGTH
    )
    average_readings = models.PositiveSmallIntegerField(
        "Cреднее показание на случай если счетчик просрочен"
    )

    price = models.PositiveSmallIntegerField("Цена за единицу")

    class Meta:
        verbose_name = "Тариф"
        verbose_name_plural = "Тарифы"
        ordering = ["id"]

    def __str__(self):
        return self.name


class Rent(DateModel):
    """Квартплата за месяц."""

    apartment = models.ForeignKey(
        Apartment,
        on_delete=models.CASCADE,
        related_name="rent",
        verbose_name="квартплата",
    )
    water_price = models.FloatField(verbose_name="Цена за воду")
    property_price = models.FloatField(
        verbose_name="Цена за содержание общего имущества"
    )

    class Meta:
        verbose_name = "Квартплата"
        verbose_name_plural = "Квартплаты"
        ordering = ["id"]

    def __str__(self):
        return (
            f"Квартплата за {self.month} - {self.year}, "
            f"квартира {self.apartment}, дом {self.apartment.house},"
        )
