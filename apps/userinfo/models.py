from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    profile = models.ImageField(upload_to='profiles/', default='profiles/default.png', blank=False)
    nickname = models.CharField(max_length=30)
    email = models.EmailField(null=True, blank=True)
    telnum = models.CharField(max_length=15, null=True, blank=True)

    def str(self):
        return self.username