#!/bin/sh
set -e

pipenv install --skip-lock --system
python manage.py makemigrations
python manage.py migrate

exec "$@"
