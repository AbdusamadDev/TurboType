from rest_framework import serializers
from django.contrib.auth.models import User


class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["username", "first_name", "last_name", "email", "password"]
        model = User


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=70, required=True)
    password = serializers.CharField(max_length=70, required=True)
