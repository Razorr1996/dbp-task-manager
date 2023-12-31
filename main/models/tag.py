from django.core.validators import validate_slug
from django.db import models

from .base import BaseModel


class Tag(BaseModel):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True, validators=[validate_slug])

    def __str__(self):
        return f"#{self.id} {self.title}"
