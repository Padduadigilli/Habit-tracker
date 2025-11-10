# habits/models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Habit(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="habits")

    def __str__(self):
        return self.name

class HabitCompletion(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name="completions")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="completions")
    completed_on = models.DateField(default=timezone.now)
    completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('habit', 'user', 'completed_on')

    def __str__(self):
        return f"{self.habit.name} completed: {self.completed}"
