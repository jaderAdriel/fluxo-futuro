from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.managements.models import Management

# Create your models here.
class User(AbstractUser):
    active_managment = models.ForeignKey(Management, on_delete=models.SET_NULL, null=True, blank=True, related_name="user_managment")