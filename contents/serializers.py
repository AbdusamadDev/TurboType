from rest_framework import serializers
from contents.models import ContentModel, CategoryModel


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ContentModel


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            "id",
            "category"
        ]
        model = CategoryModel
