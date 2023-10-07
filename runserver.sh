#!/bin/bash

env/bin/python manage.py makemigrations
env/bin/python manage.py migrate

env/bin/python manage.py runserver