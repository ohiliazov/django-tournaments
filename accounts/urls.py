from django.urls import path

from accounts.views import user_profile

urlpatterns = [
    path("profile/", user_profile),
]
