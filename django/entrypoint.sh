#!/bin/sh

python manage.py makemigrations
python manage.py migrate
python manage.py scrap
python manage.py create_admin

exec "$@"
