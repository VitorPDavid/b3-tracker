#! /bin/bash
python /b3_tracker/manage.py migrate
python /b3_tracker/manage.py runserver 0.0.0.0:8000

exec "$@"
