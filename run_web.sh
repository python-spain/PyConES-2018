#!/bin/sh

python manage.py migrate
python manage.py collectstatic --noinput
exec DJANGO_SETTINGS_MODULE=pyconesweb.prod gunicorn pyconesweb.wsgi -b 0.0.0.0:8000