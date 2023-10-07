from rest_framework import viewsets

from .serializers import DemandSerializer
from ..models import Demand


class DemandViewset(viewsets.ModelViewSet):
    queryset = Demand.objects.all()
    serializer_class = DemandSerializer
