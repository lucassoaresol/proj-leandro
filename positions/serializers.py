from rest_framework import serializers
from .models import Position


class PositionSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        postion_data = validated_data.pop("name")
        position = Position.objects.filter(
            name__iexact=postion_data,
        ).first()

        if not position:
            position = Position.objects.create(name=postion_data)

        return position

    class Meta:
        model = Position
        fields = [
            "id",
            "name",
        ]
