from django.contrib.auth.models import AbstractUser
from django.db import models

from .base import BaseModel


class User(AbstractUser, BaseModel):
    class Roles(models.TextChoices):
        DEVELOPER = "developer"
        MANAGER = "manager"
        ADMIN = "admin"

    role = models.CharField(
        max_length=255, default=Roles.DEVELOPER, choices=Roles.choices
    )

    def __str__(self):
        return f"#{self.id} {self.get_full_name()}"
