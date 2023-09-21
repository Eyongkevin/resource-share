from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    title = models.CharField(max_length=100, null=True, blank=True, help_text="Your profession")
    bio = models.TextField(default='', null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['username']
