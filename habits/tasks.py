from celery import shared_task
from habits.services import telegram_check_updates, habit_scheduler


@shared_task(name="check_habit_time")
def check_habit_time():
    telegram_check_updates()
    habit_scheduler()
