from django.urls import path
from contents import views

urlpatterns = [
    path("create/", views.ContentCreateAPIView.as_view()),
    path("<int:pk>/update/", views.ContentUpdateAPIView.as_view()),
    path("categories/create/", views.CategoryCreateAPIView.as_view()),
    path("list/", views.ContentListAPIView.as_view()),
]
