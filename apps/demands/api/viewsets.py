from rest_framework import viewsets

from .serializers import DemandSerializer
from ..models import Demand

from rest_framework.permissions import AllowAny

from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework.serializers import ValidationError
from rest_framework.exceptions import MethodNotAllowed

from django.shortcuts import get_object_or_404


class DemandViewset(viewsets.ModelViewSet):
    queryset = Demand.objects.all()
    serializer_class = DemandSerializer

    http_method_names = [
        "get",
        "post",
        "patch",
    ]

    def get_permissions(self):
        if self.action in ["create", "list", "retrieve"]:
            return [AllowAny()]
        return super().get_permissions()

    def partial_update(self, request, *args, **kwargs):
        if action != "update_status":
            raise MethodNotAllowed("PATCH")
        return super().partial_update(request, *args, **kwargs)

    @action(detail=True, methods=["patch"])
    def update_status(self, request, pk=None):
        # falta agora so fazer com que essa action seja acessivel apenas para admins
        demand = self.get_object()

        status = request.data.get("status")
        rejection_reason = request.data.get("rejection_reason")

        if status is None:
            raise ValidationError({"error": "status is mandatory"})

        demand.status = status

        if rejection_reason is None and status == 3:  # status == 3 (REFUSED)
            raise ValidationError(
                {"error": "rejection_reason is mandatory when status is 3 (REFUSED)"}
            )

        demand.rejection_reason = rejection_reason

        demand.save()

        serializer = self.get_serializer(demand)
        return Response(serializer.data)

    @action(detail=False, methods=["get"], url_path="code/(?P<code>[^/.]+)")
    def filter_by_code(self, request, code=None):
        demand = get_object_or_404(Demand, code=code)
        serializer = self.get_serializer(demand)
        return Response(serializer.data)
