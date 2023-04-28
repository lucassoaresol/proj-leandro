from rest_framework.exceptions import ParseError
from rest_framework import serializers
from .models import User, Role


def choices_error_message(choices_class):
    valid_choices = [choice[0] for choice in choices_class.choices]
    message = ", ".join(valid_choices).rsplit(",", 1)

    return "Escolher entre " + " e".join(message) + "."


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data) -> User:
        if validated_data.get("role") == "Administrator":
            user_obj = User.objects.create_superuser(**validated_data)
            return user_obj

        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            if not self.context["request"].user.is_superuser:
                if key == "role":
                    raise ParseError("User is not allowed to change his role")
                if key == "is_active":
                    raise ParseError("User is not allowed to change his is_active")

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
            "first_name",
            "last_name",
            "email",
            "phone",
            "role",
            "is_active",
            "is_default",
            "date_joined",
        ]
        read_only_fields = [
            "is_default",
            "date_joined",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "role": {
                "error_messages": {
                    "invalid_choice": choices_error_message(Role),
                }
            },
        }
