from django.urls import path, include

from . import views
from .api.routers import router

app_urls = [
    # define your app urls here
]

urlpatterns = [
    path("demands/", include(app_urls)),
    path("api/", include(router.urls)),
]
