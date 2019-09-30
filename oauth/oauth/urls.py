from django.contrib import admin
from django.urls import include, path

from o2.urls import urlpatterns as o2_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("o/", include("oauth2_provider.urls", namespace="oauth2_provider")),
    path("", include(o2_urls)),
]
