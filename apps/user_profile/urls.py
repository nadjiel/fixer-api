from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import *

from .api.routers import router

app_urls = [
    path("registration/", RegistrationView.as_view(), name="registration"),
]

django_auth_urls = [
    path("", include("django.contrib.auth.urls")),
]

drf_jwt_auth_urls = [
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh_token/", TokenRefreshView.as_view(), name="token_refresh"),
]

urlpatterns = [
    path("", include(app_urls)),
    path("", include(django_auth_urls)),
    path("api/", include(router.urls)),
    path("api/", include(drf_jwt_auth_urls)),
]
