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

    # Implementation of a filter by category suggested by
    # https://claude.ai/chat/364c0ad0-f66a-4a27-8bb8-0f85f530a6f8
    def get_queryset(self):
        queryset = Service.objects.all()
        category = self.request.query_params.get("category")

        if category is not None:
            queryset = queryset.filter(category=category)

        return queryset
