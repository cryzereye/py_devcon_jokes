# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("alljokes/", views.all_jokes),
    path("random/", views.random_joke),
    path("joke_for/<sex>", views.joke_for),
]