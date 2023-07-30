# import json
# from datetime import datetime, timedelta
#
# from django_celery_beat.models import PeriodicTask, \
#     IntervalSchedule
#
# # Создаем интервал для повтора
# schedule, created = IntervalSchedule.objects.get_or_create(
#      every=1,
#      period=IntervalSchedule.SECONDS,
#  )
#
# # Создаем задачу для повторения
# PeriodicTask.objects.create(
#      interval=schedule,
#      name='Importing contacts',
#      task='habits.tasks.send_information',
#      args=json.dumps(['arg1', 'arg2']),
#      kwargs=json.dumps({
#         'be_careful': True,
#      }),
#      expires=datetime.utcnow() + timedelta(seconds=30)
#  )