import os
import django
from django.conf import settings
from django.core.management import execute_from_command_line
from django.shortcuts import render, redirect, get_object_or_404
from django.db import models, connection
from django.urls import path
from django.utils.crypto import get_random_string
from django.contrib.auth.hashers import make_password, check_password

# Django Settings Configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEBUG = True

settings.configure(
    BASE_DIR=BASE_DIR,
    DEBUG=DEBUG,
    SECRET_KEY=get_random_string(50),
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=['*'],
    INSTALLED_APPS=[
        "django.contrib.contenttypes",
        "django.contrib.staticfiles",
        "django.contrib.sessions",
        "django.contrib.messages",
    ],
    MIDDLEWARE=[
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
    ],
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    },
    TEMPLATES=[
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [os.path.join(BASE_DIR, "templates")],
            "APP_DIRS": True,
        }
    ],
    STATIC_URL="/static/",
    STATICFILES_DIRS=[os.path.join(BASE_DIR, "static")],
)

# Initialize Django
django.setup()



# Run Django Server
if __name__ == "__main__":
    execute_from_command_line(["manage.py", "migrate", "sessions"])
    execute_from_command_line(["manage.py", "runserver","0.0.0.0:8000"])
