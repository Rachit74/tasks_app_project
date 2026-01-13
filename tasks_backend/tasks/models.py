from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    STATUS_CHOICES = [
        ("todo", "To Do"),
        ("in_progress", "In progress"),
        ("done", "Done"),
    ]

    title = models.CharField(max_length=200, null=False)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="todo"
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="tasks"
    )

    def __str__(self):
        return self.title
