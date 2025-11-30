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
        # Lets user and code as readonly, as suggested by Claude,
        # in the second question of this Chat:
        # https://claude.ai/share/0431669e-79f4-4391-93e6-ac9c677c6710
        read_only_fields = ['user', 'code']
        # exclude = ["id"]
