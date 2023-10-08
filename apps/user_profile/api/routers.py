from rest_framework.routers import DefaultRouter

from .viewsets import UserViewset

router = DefaultRouter()
router.register(r"users", UserViewset, basename="api-users")
