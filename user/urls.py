from django.urls import path
from .views import CustomUserCreateView


urlpatterns = [
    path("", CustomUserCreateView.as_view())
]
