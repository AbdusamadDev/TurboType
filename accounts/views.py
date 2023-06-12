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


class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        print(request.user.is_authenticated)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return Response({'message': 'User logged in successfully'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(APIView):
    model = User

    def get(self, request, *args, **kwargs):
        logout(request)
        return Response(data={"msg": "User logged out successfully!"}, status=status.HTTP_200_OK)
