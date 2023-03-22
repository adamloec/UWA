from django.db import models
from django.contrib.auth.models import AbstractUser

class AppUser(AbstractUser):
    has_subscription = models.BooleanField(default=False)