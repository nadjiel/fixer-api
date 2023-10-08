from rest_framework import serializers

from ..models import Demand, Support


class SupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Support
        fields = "__all__"


class DemandSerializer(serializers.ModelSerializer):
    supports = serializers.SerializerMethodField()
    supported_by_logged_user = serializers.SerializerMethodField()

    def get_supports(self, obj):
        return obj.supports.count()

    def get_supported_by_logged_user(self, obj):
        logged_user = self.context["request"].user
        return Support.objects.filter(user=logged_user.id).count() > 0

    class Meta:
        model = Demand
        fields = "__all__"
        # exclude = ["id"]
