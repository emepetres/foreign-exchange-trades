#!/bin/bash
set -e

pipenv install --dev
pipenv run python manage.py makemigrations
pipenv run python manage.py migrate
pipenv run python manage.py createsuperuser
