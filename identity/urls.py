# urls.py

from django.urls import path
from .views import CustomLoginView, CustomLogoutView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('/login', obtain_auth_token, name='custom-login'),
    path('/logout', CustomLogoutView.as_view(), name='custom-logout'),
]
