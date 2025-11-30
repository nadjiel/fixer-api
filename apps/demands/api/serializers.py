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

        # Check if user is authenticated first
        if not logged_user.is_authenticated:
            return False

        # Check if this specific demand is supported by the logged user
        return obj.supports.filter(user=logged_user).exists()

    class Meta:
        model = Demand
        fields = "__all__"
        # Lets user and code as readonly, as suggested by Claude,
        # in the second question of this Chat:
        # https://claude.ai/share/0431669e-79f4-4391-93e6-ac9c677c6710
        read_only_fields = ['user', 'code']
        # exclude = ["id"]
