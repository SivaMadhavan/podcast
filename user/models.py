from django.contrib.auth.models import AbstractUser
from django.db import models
from uuid import uuid4, UUID


class User(AbstractUser):
    uuid = models.UUIDField(primary_key=True, unique=True, default=uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "users"

    def __str__(self):
        return self.username

    def create(self, request, *args, **kwargs):
        data = request.data
        user = User.objects.create(username=data.get("username"),email=data.get("email"))
        user.set_password(data.get('password'))
        user.save()
        return {"message": "User registered successfully"}
