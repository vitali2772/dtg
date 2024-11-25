from django.contrib import admin
from .models import TodoItem

# Register your models here.
# Nachdem models registriert wurden oder datenbank models verändert wurden, 
# muss im terminal folgendes ausgeführt werden: python manage.py makemigrations,
# danach python manage.py migrate

admin.site.register(TodoItem)