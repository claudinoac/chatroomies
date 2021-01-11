FROM python:3.8-alpine

RUN mkdir /code
WORKDIR /code
COPY ./requirements /code/requirements
RUN apk add build-base && pip install -r requirements/development.txt
