from rest_framework import viewsets, permissions
from .serializers import UserSerializer, UserReadSerializer

from django.contrib.auth import get_user_model

User = get_user_model()

from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework.serializers import ValidationError


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [permissions.AllowAny()]
        return super().get_permissions()

    @action(detail=False, methods=["get"])
    def me(self, request):
        user = self.request.user
        print(user)
        print("A")
        print(request.user)
        serializer = UserReadSerializer(user)
        return Response(serializer.data)
