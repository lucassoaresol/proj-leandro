from django.shortcuts import get_object_or_404
from rest_framework import serializers
from departments.models import Department
from departments.serializers import DepartmentSerializer
from positions.models import Position
from positions.serializers import PositionSerializer
from .models import Scheme, Status


def choices_error_message(choices_class):
    valid_choices = [choice[0] for choice in choices_class.choices]
    message = ", ".join(valid_choices).rsplit(",", 1)

    return "Escolher entre " + " e".join(message) + "."


class SchemeSerializer(serializers.ModelSerializer):
    departments = DepartmentSerializer(many=True, read_only=True)
    positions = PositionSerializer(many=True, read_only=True)
    departments_id = serializers.ListField(
        child=serializers.IntegerField(), write_only=True
    )
    positions_id = serializers.ListField(
        child=serializers.IntegerField(), write_only=True
    )

    def create(self, validated_data) -> Scheme:
        departments_id = validated_data.pop("departments_id")
        positions_id = validated_data.pop("positions_id")
        scheme = Scheme.objects.create(**validated_data)

        for id in departments_id:
            department = get_object_or_404(Department, id=id)
            scheme.departments.add(department)

        for id in positions_id:
            position = get_object_or_404(Position, id=id)
            scheme.positions.add(position)

        return scheme

    class Meta:
        model = Scheme
        fields = [
            "id",
            "name",
            "num_criterion",
            "status",
            "created_at",
            "finished_at",
            "departments_id",
            "positions_id",
            "departments",
            "positions",
        ]
        read_only_fields = [
            "created_at",
        ]
        extra_kwargs = {
            "status": {
                "error_messages": {
                    "invalid_choice": choices_error_message(Status),
                }
            },
        }
