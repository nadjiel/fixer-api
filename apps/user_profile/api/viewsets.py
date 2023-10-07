from rest_framework import viewsets, permissions
from .serializers import UserSerializer

from django.contrib.auth import get_user_model

User = get_user_model()


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [permissions.AllowAny()]
        return super().get_permissions()
