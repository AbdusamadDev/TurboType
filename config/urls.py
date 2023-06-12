
from django.contrib import admin
from django.urls import path,include
from feedback.urls import FeedbackAPIView
from contents.urls import ContentsAPIView

from contents.views import home

urlpatterns = [
    path("", home, name="homepage"),
    path('admin/', admin.site.urls),
    path('feedbacks/',include("feedback.urls")),
    path('contents/',include("contents.urls")),
    
]
