FROM python:latest

MAINTAINER mass10

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get upgrade && pip install uwsgi

COPY app /app

WORKDIR /app

CMD uwsgi --http :8080 --file /app/main.py

