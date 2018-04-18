#!/bin/sh

python manage.py migrate
python manage.py collectstatic --noinput
exec gunicorn --env DJANGO_SETTINGS_MODULE=pyconesweb.prod pyconesweb.wsgi -b 0.0.0.0:8000