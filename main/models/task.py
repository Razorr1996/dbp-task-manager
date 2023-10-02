from django.db import models

from .base import BaseModel
from .tag import Tag
from .user import User


class Task(BaseModel):
    class State(models.TextChoices):
        NEW_TASK = "new_task", "New Task"
        IN_DEVELOPMENT = "in_development", "In Development"
        IN_QA = "in_qa", "in QA"
        IN_CODE_REVIEW = "in_code_review", "in Code Review"
        READY_FOR_RELEASE = "ready_for_release", "Ready for Release"
        RELEASED = "released", "Released"
        ARCHIVED = "archived", "Archived"

    class Priority(models.IntegerChoices):
        LOW = 1
        MEDIUM = 2
        HIGH = 3

    title = models.CharField(blank=True, max_length=255)
    description = models.TextField(blank=True, default="")
    deadline_at = models.DateField(null=True)
    state = models.CharField(
        max_length=255, default=State.NEW_TASK, choices=State.choices
    )
    priority = models.IntegerField(default=Priority.MEDIUM, choices=Priority.choices)
    author = models.ForeignKey(
        User, null=True, on_delete=models.SET_NULL, related_name="created_tasks"
    )
    assignee = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="assigned_tasks",
    )
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f"#{self.id} {self.title}"
