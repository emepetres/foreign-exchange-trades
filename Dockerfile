# pull official base image
FROM python:3.7-alpine

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /usr/src/fetrades

# setup dependencies
RUN pip install --upgrade pip
RUN pip install pipenv

# copy application
COPY fetrades/ /usr/src/fetrades/

ENTRYPOINT ["/usr/src/fetrades/entrypoint.sh"]
