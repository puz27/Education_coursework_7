# from config import settings
import requests
from habits.models import Habit
from users.models import Users
from datetime import datetime


# # TOKEN = settings.TELEGRAM_TOKEN
TELEGRAM_TOKEN = "6692975026:AAGSJJtkFNS2oc0w8P7jyxjFYTB7Nta973M"


def habit_scheduler():
    current_time = datetime.now()
    for habit in Habit.objects.all():
        print("-------------------------------------------------------------------------")
        # DAILY HABIT
        if habit.frequency == "DAILY":
            print(f'HABIT TIME: {habit.time.strftime("%H:%M")}')
            print(f'CURRENT TIME: {current_time.strftime("%H:%M")}')
            print(f'CHAT ID: {habit.owner.chat_id}')
            print(f'ACTION: {habit.action}')
            print(f'PLACE: {habit.place}')
            if habit.time.strftime("%H:%M") == current_time.strftime("%H:%M"):
                print("SEND MESSAGE TO TELEGRAM")
                chat_id = habit.owner.chat_id
                message = habit
                url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
                requests.get(url)

        # WEEK DAY HABIT
        else:
            today = ""
            # check current day
            if datetime.today().weekday() == 0:
                today = "MONDAY"
            elif datetime.today().weekday() == 1:
                today = "TUESDAY"
            elif datetime.today().weekday() == 2:
                today = "WEDNESDAY"
            elif datetime.today().weekday() == 3:
                today = "THURSDAY"
            elif datetime.today().weekday() == 4:
                today = "FRIDAY"
            elif datetime.today().weekday() == 5:
                today = "SATURDAY"
            elif datetime.today().weekday() == 6:
                today = "SUNDAY"

            if habit.frequency == today:
                print(today)
                print(f'HABIT TIME: {habit.time.strftime("%H:%M")}')
                print(f'CURRENT TIME: {current_time.strftime("%H:%M")}')
                print(f'CHAT ID: {habit.owner.chat_id}')
                print(f'ACTION: {habit.action}')
                print(f'PLACE: {habit.place}')
                if habit.time.strftime("%H:%M") == current_time.strftime("%H:%M"):
                    print("SEND MESSAGE TO TELEGRAM")
                    chat_id = habit.owner.chat_id
                    message = habit
                    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
                    requests.get(url)
    print("-------------------------------------------------------------------------")


def telegram_check_updates():
    url_get_updates = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates"
    response = requests.get(url_get_updates)
    if response.status_code == 200:
        for i in response.json()["result"]:
            # print(i)
            telegram_user_chat_id = response.json()["result"][0]["message"]["from"]["id"]
            telegram_user_name = response.json()["result"][0]["message"]["from"]["username"]
            print(telegram_user_chat_id, telegram_user_name)

            user = Users.objects.get(telegram_user_name=telegram_user_name)
            if user.chat_id is None:
                user.chat_id = telegram_user_chat_id
                user.save()


# chat_id = "448121994"
# message = "TEST"
# #https://api.telegram.org/bot{ваш ключ}/getUpdates
# url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={chat_id}&text={message}"


# get information about telegram users
def check_habit_time():
    # telegram_check_updates()

    habit_scheduler()
