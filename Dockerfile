# FROM python:3.10

# WORKDIR /app

# COPY requirements.txt .
# RUN pip install -r requirements.txt --no-cache-dir
# COPY . .

# CMD ["gunicorn", "--bind", "0.0.0.0:9000", "bicycle_rent_service.wsgi"]

FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

CMD ["gunicorn", "idp.wsgi:application", "--bind", "0.0.0.0:8000"]
