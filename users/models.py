from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name="user Email")
    chat_id = models.IntegerField(unique=True, blank=True, null=True, default=None)
    telegram_user_name = models.CharField(max_length=100, null=False, blank=False, unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = "users"
        verbose_name_plural = 'users'

