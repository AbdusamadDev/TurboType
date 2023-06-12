from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from contents.serializers import ContentCreateSerializer
from contents.models import ContentModel


class ContentCreateAPIView(CreateAPIView):
    serializer_class = ContentCreateSerializer
    model = ContentModel
    queryset = ContentModel.objects.all()
    permission_classes = [IsAuthenticated]
