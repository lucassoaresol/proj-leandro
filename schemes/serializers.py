from rest_framework import serializers
from departments.serializers import DepartmentSerializer
from .models import Scheme, Status


def choices_error_message(choices_class):
    valid_choices = [choice[0] for choice in choices_class.choices]
    message = ", ".join(valid_choices).rsplit(",", 1)

    return "Escolher entre " + " e".join(message) + "."


class SchemeSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)

    class Meta:
        model = Scheme
        fields = [
            "id",
            "name",
            "status",
            "created_at",
            "finished_at",
            "department",
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
