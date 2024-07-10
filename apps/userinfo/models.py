from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    profile = models.ImageField(upload_to='profiles/', default='profiles/default.png', blank=False)
    nickname = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    telnum = models.CharField(max_length=15, unique=False, null=True, blank=True)

    def __str__(self):
        return self.username
