FROM python:3.10-alpine3.18

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

WORKDIR /delivery_service
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .


CMD gunicorn delivery_service.wsgi:application --bind 0.0.0.0:8000