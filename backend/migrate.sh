#!/bin/sh
python manage.py collectstatic
pip install gunicorn



