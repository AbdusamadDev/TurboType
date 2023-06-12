from django.contrib import admin
from django.urls import path
from .views import FeedbackAPIView



urlpatterns = [
    
    path("create/",FeedbackAPIView.as_view(),name="create")
] 
