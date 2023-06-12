<<<<<<< HEAD

from django.contrib import admin
from django.urls import path,include
from feedback.urls import FeedbackAPIView
from contents.urls import ContentsAPIView

from contents.views import home
=======
from django.contrib import admin
from django.urls import path, include
>>>>>>> b76fcb9a0111a77b80b50cfd58036a0cb043b823

urlpatterns = [
    path("", home, name="homepage"),
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('feedbacks/',include("feedback.urls")),
    path('contents/',include("contents.urls")),
    
=======
    path("accounts/", include("accounts.urls")),
    path("contents/", include("contents.urls")),
>>>>>>> b76fcb9a0111a77b80b50cfd58036a0cb043b823
]
