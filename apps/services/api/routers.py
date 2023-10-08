from rest_framework import routers

from .viewsets import ServiceViewset


router = routers.DefaultRouter()
router.register(r"services", ServiceViewset, basename="api-services")
