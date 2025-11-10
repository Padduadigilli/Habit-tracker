# habits/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.core.mail import send_mail
from .models import HabitCompletion

@receiver(post_save, sender=HabitCompletion)
def send_reminder(sender, instance, created, **kwargs):
    if not instance.completed:
        # Send email reminder (for example)
        send_mail(
            'Reminder to Complete Your Habit',
            f'Hi {instance.user.username}, don\'t forget to complete your habit: {instance.habit.name} today.',
            'from@example.com',
            [instance.user.email],
            fail_silently=False,
        )
