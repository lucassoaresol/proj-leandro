from rest_framework import serializers
from categories.serializers import CategorySerializer
from categories.models import Category
from options.models import Option
from .models import Criterion


class CriterionSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    def create(self, validated_data) -> Criterion:
        category_data = validated_data.pop("category")
        options_data = category_data.pop("options")
        category = Category.objects.filter(
            name__iexact=category_data["name"],
        ).first()

        if not category:
            category = Category.objects.create(**category_data)

        options_list = [Option(**values, category=category) for values in options_data]
        Option.objects.bulk_create(options_list)

        return Criterion.objects.create(**validated_data, category=category)

    class Meta:
        model = Criterion
        fields = [
            "id",
            "description",
            "category",
        ]
