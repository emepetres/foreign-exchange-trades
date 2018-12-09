# pull official base image
FROM python:3.7-alpine

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /usr/src/fetrades

# install psycopg2 (https://github.com/psycopg/psycopg2/issues/684)
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk del build-deps

# copy application
COPY fetrades/ /usr/src/fetrades/

# setup dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --skip-lock --system

ENTRYPOINT ["/usr/src/fetrades/entrypoint.sh"]
