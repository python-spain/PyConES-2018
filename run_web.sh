#!/bin/sh

python manage.py migrate
python manage.py collectstatic --noinput
exec gunicorn pyconesweb.wsgi -b 0.0.0.0:8000