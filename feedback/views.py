from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status


class FeedbackCreateAPIView(CreateAPIView):
    serializer_class = FeedbackSerializer
