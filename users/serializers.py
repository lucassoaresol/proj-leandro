from rest_framework.exceptions import ParseError
from rest_framework import serializers
from departments.serializers import DepartmentSerializer
from departments.models import Department
from positions.serializers import PositionSerializer
from positions.models import Position
from .models import User, Role


def choices_error_message(choices_class):
    valid_choices = [choice[0] for choice in choices_class.choices]
    message = ", ".join(valid_choices).rsplit(",", 1)

    return "Escolher entre " + " e".join(message) + "."


class UserSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(max_length=128, required=False)
    department = DepartmentSerializer()
    position = PositionSerializer()

    def create(self, validated_data) -> User:
        department_data = validated_data.pop("department")
        department = Department.objects.filter(
            name__iexact=department_data["name"]
        ).first()

        if not department:
            department = Department.objects.create(**department_data)

        position_data = validated_data.pop("position")
        position = Position.objects.filter(
            name__iexact=position_data["name"],
        ).first()

        if not position:
            position = Position.objects.create(**position_data)

        position.departments.add(department)

        if validated_data.get("role") == "Administrator":
            user_obj = User.objects.create_superuser(
                **validated_data, department=department, position=position
            )
            return user_obj

        return User.objects.create_user(
            **validated_data, department=department, position=position
        )

    def update(self, instance: User, validated_data: dict) -> User:
        try:
            old_password = validated_data.pop("old_password")
            if old_password:
                if not instance.check_password(old_password):
                    raise ParseError("old password does not match")
        except KeyError:
            ...
        for key, value in validated_data.items():
            if not self.context["request"].user.is_superuser:
                if key == "role":
                    raise ParseError("User is not allowed to change his role")
                if key == "is_active":
                    raise ParseError(
                        "User is not allowed to change his is_active",
                    )

            setattr(instance, key, value)

            if key == "password":
                instance.set_password(value)

            instance.save()

        return instance

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
            "old_password",
            "first_name",
            "last_name",
            "email",
            "phone",
            "role",
            "is_active",
            "is_first_access",
            "is_expired",
            "date_joined",
            "date_expired",
            "department",
            "position",
        ]
        read_only_fields = [
            "date_joined",
            "date_expired",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "role": {
                "error_messages": {
                    "invalid_choice": choices_error_message(Role),
                }
            },
        }
