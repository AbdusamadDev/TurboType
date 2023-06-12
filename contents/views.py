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

    # def post(self, request, *args, **kwargs):
    #     serializer = self.serializer_class(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     category_id = CategoryModel.objects.get(pk=serializer.validated_data.get("category")).id

    def get_serializer_context(self):
        print("Function is working")
        category_id = CategoryModel.objects.get(pk=self.request.data.get("category"))
        return super().get_serializer_context().update({"category": category_id})


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
