#!/bin/sh

python manage.py migrate
python manage.py collectstatic --noinput --clear
python manage.py compilemessages
exec gunicorn --log-level=debug --timeout 10 --env DJANGO_SETTINGS_MODULE=pyconesweb.prod pyconesweb.wsgi -b 0.0.0.0:8000