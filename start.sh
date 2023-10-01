#!/usr/bin/env bash

echo "Run migrations"
flask db upgrade

echo "Run flask app"
gunicorn -w 4 -b 0.0.0.0:80 app:app