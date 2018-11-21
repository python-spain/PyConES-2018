#!/bin/sh

python manage.py migrate
python manage.py collectstatic --noinput --clear
python manage.py compilemessages
exec gunicorn pyconesweb.wsgi \
    --worker-class gevent \
    --workers 2 \
    --log-level=debug \
    --timeout 60 \
    --env DJANGO_SETTINGS_MODULE=pyconesweb.prod \
    -b 0.0.0.0:8000