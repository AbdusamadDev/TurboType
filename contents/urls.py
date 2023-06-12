from django.urls import path

from contents import views
print("urls started")

urlpatterns = [
    path("create/", views.ContentCreateAPIView.as_view()),
]
