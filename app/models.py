from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    organization_type = models.CharField(max_length=255)
    organization_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    address = models.TextField()
    groups = models.ManyToManyField(Group, related_name='custom_user_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set', blank=True)

    def __str__(self):
        return self.username
