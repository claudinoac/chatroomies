FROM python:3.8-alpine

RUN mkdir /code
WORKDIR /code
COPY ./requirements /code/requirements
RUN pip install -r requirements/development.txt
