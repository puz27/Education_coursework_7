from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name="user Email")
    phone = models.CharField(max_length=50, verbose_name="user phone number", null=True, blank=True)
    country = models.CharField(max_length=50, verbose_name="user country", null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
