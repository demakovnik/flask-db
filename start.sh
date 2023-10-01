#!/usr/bin/env bash

echo "Run migrations"
flask db upgrade

echo "Run flask app"
python main.py