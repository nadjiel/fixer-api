from rest_framework import viewsets

from .serializers import ServiceSerializer
from ..models import Service

from rest_framework.permissions import AllowAny


class ServiceViewset(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return super().get_permissions()
