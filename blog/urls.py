# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("post/<int:id>", views.get_post),
    path("greet/<name>", views.greet),
]