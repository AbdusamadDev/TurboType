from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('feedbacks/', include("feedback.urls")),
    path('contents/', include("contents.urls")),
]
