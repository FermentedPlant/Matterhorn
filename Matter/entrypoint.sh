#!/bin/bash

echo "Apply database makemigrations" 
python manage.py makemigrations

echo "Apply database migrations" 
python manage.py migrate

exec "$@"