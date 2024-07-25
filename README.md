# Communal_services
Приложение для коммунальных служб. Позволяет смотреть и редактировать информацию
о домах/квартирах/счетчиках и тарифах, а также рассчитывать квартплату.


## Реализованные функции:
- Созданы модели Дом, Квартира, Счетчик, Показания счетчика, Тариф и Квартплата.
- После применения миграций в базу автоматически добавляются тестовые данные, в т.ч. суперпользователь. В админку можно зайти используя пару:  
{  
  "email": "admin@ad.ru",  
  "password": "admin"  
}
- С документацией запущенного проекта можно ознакомиться здесь:  
http://127.0.0.1:8000/swagger/

-  Для расчета квартплаты по дому за месяц:
```
POST /api/v1/rent/get_rent_per_month/
В запрос передать год, месяц и номер дома:
{
  "year": "2024",
  "month": "6",
  "house_id": "2"
}
```

-  Для получения полной информации по домам:
```
GET /api/v1/house

```

- Можно получать и создавать экземпляры ко всем моделям отдельно



##  Запуск проекта

### Запуск в контейнерах

1. Убедиться, что установлен Docker
2. Клонировать репозиторий и перейти в него
3. Создать .env и заполнить по образцу .env.example
4. Запустить docker-compose.yml
5. Выполнить миграции
```
git clone https://github.com/Anastasia289/communal_services.git
cd communal_services/backend
docker compose up
docker compose exec backend python manage.py migrate

```

## Технологии:
- Backend: Django, Django Rest Framework
- База данных: PostgreSQL
- Контейнеризация: Docker

[![My Skills](https://skillicons.dev/icons?i=py,docker,postgres,django,)](https://skillicons.dev)
