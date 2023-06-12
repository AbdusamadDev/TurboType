from contents.models import ContentModel, CategoryModel
from contents.serializers import ContentSerializer, CategorySerializer
from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveAPIView,
    ListAPIView,
)


class ContentCreateAPIView(CreateAPIView):
    serializer_class = ContentSerializer
    model = ContentModel
    queryset = ContentModel.objects.all()


class ContentUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = ContentSerializer
    model = ContentModel
    queryset = ContentModel.objects.all()
    lookup_url_kwarg = "pk"


class ContentRetrieveAPIView(RetrieveAPIView):
    lookup_url_kwarg = "pk"
    model = ContentModel
    queryset = ContentModel.objects.all()


class ContentListAPIView(ListAPIView):
    lookup_url_kwarg = "pk"
    model = ContentModel

    def get_queryset(self):
        queryset = self.queryset.filter(category_id=self.kwargs.get("pk"))
        return queryset


class CategoryCreateAPIView(CreateAPIView):
    serializer_class = CategorySerializer
    model = CategoryModel
    queryset = CategoryModel.objects.all()
