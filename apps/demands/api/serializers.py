from rest_framework import serializers

from ..models import Demand, Support


class DemandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demand
        fields = "__all__"
        # exclude = ["id"]


class SupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Support
        fields = "__all__"
