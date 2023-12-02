# urls.py

from django.urls import path
from .views import RegisterView, LogoutAPIView, LoginAPIView, VerificationView

urlpatterns = [
    path('register', RegisterView.as_view(), name="register"),
    path('verification', VerificationView.as_view(), name="email-verify"),
    path('login', LoginAPIView.as_view(), name="login"),
    path('logout', LogoutAPIView.as_view(), name="logout"),
]
