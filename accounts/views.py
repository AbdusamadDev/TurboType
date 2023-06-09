from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

from accounts.serializers import UserCreationSerializer, UserLoginSerializer


class RegisterAPIView(CreateAPIView):
    model = User
    queryset = User.objects.all()
    serializer_class = UserCreationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        username = serializer.validated_data.get("username")
        password = serializer.validated_data.get("password")
        user = authenticate(username=username, password=password)
        print(user)
        if user:
            login(request, user)
            return Response(
                data={"msg": "User created successfully and logged in"},
                status=status.HTTP_201_CREATED
            )
        return Response(
            data={"msg": "User Creation process failed"}, status=status.HTTP_400_BAD_REQUEST
        )

    def perform_create(self, serializer):
        serializer.save()


class LoginAPIView(APIView):
    model = User
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get("email")
        password = serializer.validated_data.get("password")
        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            return Response(data={"msg": "User logged in successfully!"}, status=status.HTTP_200_OK)
        return Response(
            data={"msg": "User authentication credentials failed!"},
            status=status.HTTP_401_UNAUTHORIZED
        )


class LogoutAPIView(APIView):
    model = User

    def get(self, request, *args, **kwargs):
        logout(request)
        return Response(data={"msg": "User logged out successfully!"}, status=status.HTTP_200_OK)
