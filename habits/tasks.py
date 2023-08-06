from celery import shared_task
from habits.models import Habit
from datetime import datetime


@shared_task(name="check_habit_time")
def check_habit_time():
    today = datetime.today().weekday()
    current_time = datetime.now().time()
    habits = Habit.objects.filter()
    for habit in habits:
        print(habit)
        print(habit.frequency)
        if habit.frequency == "DAILY":
            if habit.time == current_time:
                print("SEND MESSAGE TO TELEGRAM")
        else:
            print(f"DAY WEEK:{today}")
            if habit.frequency == today:
                if habit.time == current_time:
                    print("SEND MESSAGE TO TELEGRAM")
                    print("SEND MESSAGE TO TELEGRAM")

