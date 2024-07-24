from django.contrib.auth import get_user_model
from django.db import models

from backend.constants import MAX_CHAR_LENGTH

User = get_user_model()


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


class WaterMeterData(models.Model):
    """Показания счетчика за несколько месяцев."""

    water_meter = models.ForeignKey(
        WaterMeter,
        on_delete=models.CASCADE,
        related_name="water_meter",
        verbose_name="счетчик",
    )
    meter_readings = models.PositiveSmallIntegerField("Показания счетчика")
    date = models.DateField(
        "Дата снятия показаний",
        auto_now_add=True,
    )
    year = models.PositiveSmallIntegerField("Год")
    month = models.PositiveSmallIntegerField("Месяц")

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


class Rent(models.Model):
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
    date = models.DateField(
        auto_now_add=True,
        verbose_name="Дата показаний",
    )
    year = models.PositiveSmallIntegerField("Год")
    month = models.PositiveSmallIntegerField("Месяц")

    class Meta:
        verbose_name = "Квартплата"
        verbose_name_plural = "Квартплаты"
        ordering = ["id"]

    def __str__(self):
        return self.number


# Квартплата включает в себя:
# Расчет за определенный месяц
# ● Водоснабжение. Рассчитывается по расходу воды за месяц
# (тариф_за_единицу_объёма × расход). Расход — это разница между показаниями
# счётчика за текущий и за предыдущий месяц.
# ● Содержание общего имущества. Рассчитывается на основе площади квартиры
# (тариф_за_единицу_площади × площадь_квартиры).
