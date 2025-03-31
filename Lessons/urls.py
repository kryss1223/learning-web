# Lessons/urls.py
from django.urls import path
from .views import ejercicio_espacios

urlpatterns = [
    path('', ejercicio_espacios, name='ejesp'),
]
