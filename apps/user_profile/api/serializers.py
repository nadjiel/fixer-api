from rest_framework import serializers

from django.contrib.auth import get_user_model

User = get_user_model()

from ..models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(write_only=True, required=False)
    picture = serializers.ImageField(write_only=True, required=False)
    email = serializers.EmailField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("id", "username", "email", "password", "phone", "picture")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        phone = validated_data.pop("phone")
        picture = validated_data.pop("picture")
        # email = validated_data.pop("email")

        user = User.objects.create(**validated_data)
        user.set_password(validated_data["password"])
        user.save()

        UserProfile.objects.create(owner=user, phone=phone, picture=picture)
        return user
