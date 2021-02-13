#!/bin/bash
set -e

echo "Let the DB start..."
sleep 2;

if [ ! -d "media" ]; then
  echo "Preparing media"
  mkdir -p media
  cp static/images/* media/ -r
fi

echo "Making migrations"
python manage.py makemigrations
python manage.py migrate

echo "Starting app"
python manage.py runserver 0.0.0.0:8000

# Deploy:
# Create superuser
