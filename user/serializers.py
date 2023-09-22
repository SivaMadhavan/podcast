from rest_framework import serializers
from rest_framework.validators import ValidationError
from django.contrib.auth import get_user_model
from django.db.models import Q
User = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def validate(self, data):
        username = data.get("username")
        email = data.get("email")
        if username and email:
            if User.objects.filter(Q(username=username) | Q(email=email)).exists():
                raise ValidationError("This username is already taken")
        return data
