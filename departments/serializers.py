from rest_framework import serializers
from .models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        department_data = validated_data.pop("name")
        department = Department.objects.filter(
            name__iexact=department_data,
        ).first()

        if not department:
            department = Department.objects.create(name=department_data)

        return department

    class Meta:
        model = Department
        fields = [
            "id",
            "name",
        ]
