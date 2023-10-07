from rest_framework import viewsets

from .serializers import DemandSerializer
from ..models import Demand

from rest_framework.permissions import AllowAny


# TODO: colocar action para apenas administradores poderem performar patch (e o patch ser apenas no status e no motivo)
class DemandViewset(viewsets.ModelViewSet):
    queryset = Demand.objects.all()
    serializer_class = DemandSerializer

    http_method_names = [
        "get",
        "post",
        "patch",
    ]

    def get_permissions(self):
        super().http_method_names
        if self.action in ["create"]:
            return [AllowAny()]
        return super().get_permissions()
