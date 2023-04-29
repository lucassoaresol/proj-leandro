from rest_framework import serializers
from .models import Criterion


class CriterionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Criterion
        fields = [
            "id",
            "value",
            "description",
        ]
