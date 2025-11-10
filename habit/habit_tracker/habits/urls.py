# habits/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.habit_list, name='habit_list'),  # List habits
    path('add/', views.add_habit, name='add_habit'),  # Add habit
    path('edit/<int:habit_id>/', views.edit_habit, name='edit_habit'),  # Edit habit
    path('delete/<int:habit_id>/', views.delete_habit, name='delete_habit'),  # Delete habit
    path('complete/<int:habit_id>/', views.complete_habit, name='complete_habit'),  # Mark habit as completed
    path('progress/<int:habit_id>/', views.habit_progress, name='habit_progress'),  # Habit progress (streaks)
]
