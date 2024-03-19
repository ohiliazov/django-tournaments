from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from django_tournaments import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("accounts/", include("allauth.socialaccount.urls")),
    path("accounts/", include("accounts.urls")),
    path("", include("tournaments.urls")),
    *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
]
