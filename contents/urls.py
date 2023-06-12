from django.contrib import admin
from django.urls import path
from .views import ContentsAPIView



urlpatterns = [
    
    path("contents/",ContentsAPIView.as_view())
] 
