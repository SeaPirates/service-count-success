FROM python:3.7.0b3-slim-stretch
MAINTAINER Daniel Silva <silva20102@gmail.com>

RUN mkdir -p /service
WORKDIR /service

COPY ./ /service
RUN . service/bin/activate

ENV FLASK_APP=src/api.py
ENV MYSQL_HOST=localhost
ENV MYSQL_PORT=3306
ENV MYSQL_USER=root
ENV MYSQL_PASS=root

EXPOSE 5000

CMD ["sh", "-c", "flask run --host=0.0.0.0"]