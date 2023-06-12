<<<<<<< HEAD
from django.contrib import admin
from django.urls import path
from .views import ContentsAPIView



urlpatterns = [
    
    path("contents/",ContentsAPIView.as_view())
] 
=======
from django.urls import path

from contents import views
print("urls started")

urlpatterns = [
    path("create/", views.ContentCreateAPIView.as_view()),
]
>>>>>>> b76fcb9a0111a77b80b50cfd58036a0cb043b823
