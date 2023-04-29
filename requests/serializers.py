from rest_framework import serializers
from schemes.serializers import SchemeSerializer
from users.serializers import UserSerializer
from criterions.serializers import CriterionSerializer
from .models import Request


class RequestSerializer(serializers.ModelSerializer):
    scheme = SchemeSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    criterion = CriterionSerializer(read_only=True)
    criterion_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Request
        fields = [
            "id",
            "is_active",
            "created_at",
            "canceled_at",
            "scheme",
            "user",
            "criterion_id",
            "criterion",
        ]
        read_only_fields = [
            "created_at",
        ]
