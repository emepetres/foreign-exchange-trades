#!/bin/bash
set -e

virtualenv3 .venv

source .venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
deactivate
