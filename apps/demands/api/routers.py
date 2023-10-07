from rest_framework import routers

from .viewsets import DemandViewset


router = routers.DefaultRouter()
router.register("demands", DemandViewset, basename="api-demands")
