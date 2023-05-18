from rest_framework import serializers
from options.serializers import OptionSerializer
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)

    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "options",
        ]
