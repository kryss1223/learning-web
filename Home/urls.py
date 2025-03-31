from django.urls import path
from Home.views import show_lessons

urlpatterns = [
    path('', show_lessons,  name='home'),
]
