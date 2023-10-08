from rest_framework import viewsets

from .serializers import DemandSerializer, SupportSerializer
from ..models import Demand, Support

from rest_framework.permissions import AllowAny

from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework.serializers import ValidationError
from rest_framework.exceptions import MethodNotAllowed

from django.shortcuts import get_object_or_404


class DemandViewset(viewsets.ModelViewSet):
    queryset = Demand.objects.all()
    serializer_class = DemandSerializer

    http_method_names = ["get", "post", "patch", "delete"]

    def get_permissions(self):
        if self.action in ["create", "list", "retrieve", "delete"]:
            return [AllowAny()]
        return super().get_permissions()

    def partial_update(self, request, *args, **kwargs):
        if action != "update_status":
            raise MethodNotAllowed("PATCH")
        return super().partial_update(request, *args, **kwargs)

    @action(detail=True, methods=["patch"])
    def update_status(self, request, pk=None):
        # falta agora so fazer com que essa action seja acessivel apenas para admins

        # logged_user = self.request.user

        # if logged_user is not None and logged_user.is_superuser == False:
        #     raise PermissionError()

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

    @action(detail=True, methods=["post"])
    def support(self, request, pk=None):
        demand = self.get_object()

        support = Support.objects.filter(user=self.request.user, demand=demand)

        if support.count() > 0:
            raise ValidationError(
                {"error": "you cannot support a single demand multiple times"}
            )

        Support.objects.create(user=self.request.user, demand=demand)
        serializer = self.get_serializer(demand)

        return Response(serializer.data)

    @action(detail=True, methods=["post"])
    def unsupport(self, request, pk=None):
        demand = self.get_object()
        support = Support.objects.filter(user=self.request.user, demand=demand)
        if support.count() > 0:
            support[0].delete()
        serializer = self.get_serializer(demand)
        return Response(serializer.data)


class SupportViewset(viewsets.ModelViewSet):
    queryset = Support.objects.all()
    serializer_class = SupportSerializer

    def get_permissions(self):
        return [AllowAny()]

    @action(detail=False, methods=["post"])
    def unsupport(self, request):
        user = request.data.get("user")
        demand = request.data.get("demand")

        support = Support.objects.filter(user=user, demand=demand)
        if support.count() > 0:
            support[0].delete()

        return Response(status=200, data={"success": "unsupported successfuly"})
