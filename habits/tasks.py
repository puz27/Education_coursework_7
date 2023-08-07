from celery import shared_task
from habits.models import Habit
from datetime import datetime
import requests
TELEGRAM_TOKEN = "6692975026:AAGSJJtkFNS2oc0w8P7jyxjFYTB7Nta973M"


@shared_task(name="check_habit_time")
def check_habit_time():
    print("RUN!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    url_get_updates = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates"
    response = requests.get(url_get_updates)
    if response.status_code == 200:
        for i in response.json()["result"]:
            print(i)
            telegram_user_chat_id = response.json()["result"][0]["message"]["from"]["id"]
            telegram_user_name = response.json()["result"][0]["message"]["from"]["username"]
            print(telegram_user_chat_id, telegram_user_name)

            user = Habit.objects.filter(telegram_user_name=telegram_user_name)
            print(user)
            user.chat_id = telegram_user_chat_id
            user.save()

    # today = datetime.today().weekday()
    # current_time = datetime.now().time()
    # habits = Habit.objects.filter()
    # for habit in habits:
    #     print(habit)
    #     print(habit.frequency)
    #     if habit.frequency == "DAILY":
    #         if habit.time == current_time:
    #             print("SEND MESSAGE TO TELEGRAM")
    #     else:
    #         print(f"DAY WEEK:{today}")
    #         if habit.frequency == today:
    #             if habit.time == current_time:
    #                 print("SEND MESSAGE TO TELEGRAM")
    #                 print("SEND MESSAGE TO TELEGRAM")

