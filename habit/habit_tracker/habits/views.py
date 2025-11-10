# habits/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta
from .models import Habit, HabitCompletion
from .forms import HabitForm

# Add a new habit
@login_required
def add_habit(request):
    if request.method == "POST":
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user  # Associate habit with the current user
            habit.save()
            return redirect('habit_list')
    else:
        form = HabitForm()
    return render(request, 'habits/add_habit.html', {'form': form})

# Edit an existing habit
@login_required
def edit_habit(request, habit_id):
    habit = Habit.objects.get(id=habit_id, user=request.user)
    if request.method == "POST":
        form = HabitForm(request.POST, instance=habit)
        if form.is_valid():
            form.save()
            return redirect('habit_list')
    else:
        form = HabitForm(instance=habit)
    return render(request, 'habits/edit_habit.html', {'form': form})

# Delete a habit
@login_required
def delete_habit(request, habit_id):
    habit = Habit.objects.get(id=habit_id, user=request.user)
    habit.delete()
    return redirect('habit_list')

# List habits for the logged-in user
@login_required
def habit_list(request):
    habits = Habit.objects.filter(user=request.user)
    return render(request, 'habits/habit_list.html', {'habits': habits})

# Mark a habit as completed for today
@login_required
def complete_habit(request, habit_id):
    habit = Habit.objects.get(id=habit_id, user=request.user)
    today = timezone.now().date()
    
    # Record completion for today (if not already completed today)
    completion, created = HabitCompletion.objects.get_or_create(
        habit=habit,
        user=request.user,
        completed_on=today,
        defaults={'completed': True}
    )
    
    if not created:  # If the habit completion already exists for today, update it
        completion.completed = True
        completion.save()

    return redirect('habit_list')

# View habit progress and streaks
@login_required
def habit_progress(request, habit_id):
    habit = Habit.objects.get(id=habit_id, user=request.user)
    completions = HabitCompletion.objects.filter(habit=habit, user=request.user).order_by('-completed_on')

    # Calculate streak
    streak = 0
    last_date = None
    for completion in completions:
        if last_date and completion.completed_on == last_date - timedelta(days=1):
            streak += 1
        elif completion.completed:
            streak = 1
        last_date = completion.completed_on

    return render(request, 'habits/habit_progress.html', {'habit': habit, 'completions': completions, 'streak': streak})
