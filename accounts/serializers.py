from rest_framework import serializers

from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["username", "first_name", "last_name", "email", "password"]
        model = User

    def save(self, **kwargs):
        user = self.Meta.model
        return user.objects.create_user(
            username=self.validated_data.get("username"),
            email=self.validated_data.get("email"),
            password=self.validated_data.get("password"),
            first_name=self.validated_data.get("first_name"),
            last_name=self.validated_data.get("last_name"),
        )


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise serializers.ValidationError("Invalid username or password.")
        else:
            raise serializers.ValidationError("Both username and password are required.")

        data['user'] = user
        return data
