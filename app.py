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


# Define User Model for Authentication
class Users(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)

    class Meta:
        app_label = "expenses_app"

# Define Expense Model
class Expense(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    amount = models.FloatField()
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = "expenses_app"
# Ensure Database Tables Exist
def create_database():
    with connection.schema_editor() as schema_editor:
        if "expenses_app_expense" in connection.introspection.table_names():
            schema_editor.delete_model(Expense)
        if "expenses_app_users" not in connection.introspection.table_names():
            schema_editor.create_model(Users)
        schema_editor.create_model(Expense)
        print("✅ Updated database tables.")

create_database()


# Authentication Views
def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if Users.objects.filter(username=username).exists():
            return render(request, "register.html", {"error": "Username already exists."})

        hashed_password = make_password(password)
        Users.objects.create(username=username, password=hashed_password)

        return redirect("login")

    return render(request, "register.html")

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = Users.objects.filter(username=username).first()

        if user and check_password(password, user.password):
            request.session["user_id"] = user.id
            return redirect("list_expenses")

        return render(request, "login.html", {"error": "Invalid username or password."})

    return render(request, "login.html")

def user_logout(request):
    request.session.flush()
    return redirect("login")

# Expense Views
def index(request):
    return render(request, "index.html")

def list_expenses(request):
    if "user_id" not in request.session:
        return redirect("login")
    user_id = request.session["user_id"]
    expenses = Expense.objects.filter(user_id=user_id).order_by("-date")
    return render(request, "list_expenses.html", {"expenses": expenses})


# Run Django Server
if __name__ == "__main__":
    execute_from_command_line(["manage.py", "migrate", "sessions"])
    execute_from_command_line(["manage.py", "runserver","0.0.0.0:8000"])
    
