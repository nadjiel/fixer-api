from rest_framework import routers

from .viewsets import DemandViewset, SupportViewset


router = routers.DefaultRouter()
router.register(r"demands", DemandViewset, basename="api-demands")
router.register(r"supports", SupportViewset, basename="api-supports")
