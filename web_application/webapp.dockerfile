FROM python:3.8-alpine

RUN mkdir -p /code/requirements
WORKDIR /code
COPY ./requirements /code/requirements
RUN apk add --update --virtual .build-deps build-base \
            gcc \
            libzmq \
            musl-dev \
            zeromq-dev \
            mariadb-client \
            mariadb-connector-c-dev \
            sqlite && \
            pip install -U pip setuptools && \
            pip install -r requirements/development.txt
EXPOSE 8080
