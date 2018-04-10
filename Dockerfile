FROM python:2.7.14-slim-stretch
MAINTAINER Daniel Silva <silva20102@gmail.com>

RUN mkdir -p /service
WORKDIR /service

COPY ./ /service
RUN pip install -r requerements

ENV FLASK_APP=src/api.py
ENV MYSQL_HOST=localhost
ENV MYSQL_PORT=3306
ENV MYSQL_USER=root
ENV MYSQL_PASS=root

EXPOSE 5000

ENTRYPOINT ["sh", "-c" ,"flask run --host=0.0.0.0"]