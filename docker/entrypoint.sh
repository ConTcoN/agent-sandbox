#!/bin/sh
set -e

echo "========================================"
echo "Starting application"
echo "========================================"

echo "Running database migrations..."
flask --app run.py db upgrade

echo "Database is up to date."

echo "Starting Gunicorn..."
exec gunicorn --bind 0.0.0.0:8000 run:app