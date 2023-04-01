from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    bio = models.TextField(null=True, blank=True)
    avatar = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return str(self.username)
