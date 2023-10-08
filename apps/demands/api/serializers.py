from rest_framework import serializers

from ..models import Demand, Support


class SupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Support
        fields = "__all__"


class DemandSerializer(serializers.ModelSerializer):
    supports = serializers.SerializerMethodField()

    def get_supports(self, obj):
        return obj.supports.count()

    class Meta:
        model = Demand
        fields = "__all__"
        # exclude = ["id"]
