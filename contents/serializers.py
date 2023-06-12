from rest_framework import serializers
from contents.models import ContentModel, CategoryModel


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ContentModel

    def update(self, instance, validated_data):
        category_id = validated_data.pop('category', None)
        if category_id:
            print("Function is wotkinasdasdasd")
            category = CategoryModel.objects.get(id=category_id)
            instance.id = category
        return super().update(instance, validated_data)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            "id",
            "category"
        ]
        model = CategoryModel

# [
#             "id", "book_name", "book_author", "book_content", "category_id", "book_page"
#         ]
