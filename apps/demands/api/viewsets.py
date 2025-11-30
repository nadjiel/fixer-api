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

    # Implementation of a filter by user suggested by
    # https://claude.ai/chat/364c0ad0-f66a-4a27-8bb8-0f85f530a6f8
    def get_queryset(self):
        queryset = super().get_queryset()

        # Filter by user ID
        user_id = self.request.query_params.get('user')
        if user_id is not None:
            queryset = queryset.filter(user_id=user_id)

        # Filter by demands supported by current user
        supported_by_me = self.request.query_params.get('supported_by_me')
        if supported_by_me and supported_by_me.lower() == 'true':
            if self.request.user.is_authenticated:
                queryset = queryset.filter(supports__user=self.request.user)
            else:
                queryset = queryset.none()  # Return empty queryset for anonymous users

        return queryset

    def get_permissions(self):
        if self.action in ["create", "list", "retrieve", "delete"]:
            return [AllowAny()]
        return super().get_permissions()

    # Makes sure to register demand creator.
    # This fix was suggested by Claude in the second question of this Chat:
    # https://claude.ai/share/0431669e-79f4-4391-93e6-ac9c677c6710
    def perform_create(self, serializer):
        # Only set user if authenticated
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            serializer.save()  # user will be None

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
