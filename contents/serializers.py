from rest_framework import serializers
from contents.models import ContentModel


class ContentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["book_name", "book_author", "book_content", "book_page"]
        model = ContentModel
