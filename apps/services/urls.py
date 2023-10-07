from django.urls import path, include

from .api.routers import router

app_urls = [
    # define your app urls here
]

urlpatterns = [
    path("api/", include(router.urls)),
]
