from celery import shared_task


@shared_task(name="check_habit_time")
def check_habit_time():
    print("Check last login user.")
