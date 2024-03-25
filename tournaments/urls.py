# example/urls.py
from django.urls import path

from tournaments.views import index

urlpatterns = [
    path("", index, name="tournaments"),
]
