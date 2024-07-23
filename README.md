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
- С документацией запущенного проекта можно будет ознакомиться по адресу:
http://127.0.0.1:8000/swagger/


##  Запуск проекта

### Запуск в контейнерах

1. Убедиться, что установлен Docker
2. Скопировать docker-compose.yml
3. Создать .env и заполнить по образцу .env.example
4. Запустить docker-compose.yml, выполнить миграции и собрать статику
```
docker compose up
docker compose exec backend python manage.py migrate
docker compose exec backend python manage.py collectstatic
docker compose exec backend cp -r /app/collected_static/. /static/

```

### Запуск без контейнеров

Клонировать репозиторий:  
https://github.com/Anastasia289/communal_services.git

Перейти в него в командной строке:  
```cd weather_up```  

Cоздать виртуальное окружение:  
```python -m venv venv ```  

Активировать виртуальное окружение:  
```source venv/scripts/activate```  

Установить зависимости из файла requirements.txt:  
```python -m pip install -r requirements.txt```

Выполнить миграции:  
``` python manage.py migrate```  

Загрузить города:  
``` python manage.py load_cities```

Запустить проект:  
```python manage.py runserver  ```

## Технологии:
- Backend: Django, Django Rest Framework
- База данных: PostgreSQL
- Контейнеризация: Docker

[![My Skills](https://skillicons.dev/icons?i=py,docker,postgres,django,)](https://skillicons.dev)
