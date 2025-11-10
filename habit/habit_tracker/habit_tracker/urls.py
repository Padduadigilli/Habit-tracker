from django.contrib import admin
from django.urls import path
from habits import views  # Correct import of views from habits app

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin URL
    path('', views.habit_list, name='habit_list'),  # Default habit list
    path('add/', views.add_habit, name='add_habit'),  # Add habit
    path('edit/<int:habit_id>/', views.edit_habit, name='edit_habit'),  # Edit habit
    path('delete/<int:habit_id>/', views.delete_habit, name='delete_habit'),  # Delete habit
    path('accounts/login/', views.CustomLoginView.as_view(), name='login'),  # Use custom login view
]
