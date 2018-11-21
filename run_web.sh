#!/bin/sh

python manage.py migrate
python manage.py collectstatic --noinput --clear
python manage.py compilemessages
exec gunicorn --worker-class eventlet --log-level=debug --timeout 60 --env DJANGO_SETTINGS_MODULE=pyconesweb.prod pyconesweb.wsgi -b 0.0.0.0:8000