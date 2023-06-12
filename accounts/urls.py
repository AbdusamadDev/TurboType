from django.urls import path
from accounts import views

urlpatterns = [
    path("register/", views.RegisterAPIView.as_view(), name="register"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", views.LogoutAPIView.as_view(), name="logout")
]
