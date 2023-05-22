from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    # admin urls
    path("admin/", admin.site.urls),
    # dbstorage
    path("", include("dbstorage.urls")),
]
