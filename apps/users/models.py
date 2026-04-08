from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    bio = models.TextField(blank=True, max_length=500)
    avatar_url = models.URLField(blank=True)
    is_banned = models.BooleanField(default=False)

    def __str__(self):
        return self.username