from django.db import models
from config import settings
import django as django


class UsualHabit:

    class HabitFrequency(models.TextChoices):
        Daily = 'DAILY'
        Weekly = 'WEEKLY'

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, verbose_name="owner of habit")
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name="place for habit")
    time = models.TimeField(default=django.utils.timezone.now, verbose_name="start time for habit")
    action = models.CharField(max_length=100, null=False, blank=False, verbose_name="habit action")
    has_pleasant = models.BooleanField(default=False, verbose_name="flag for pleasant habit")
    link_pleasant = models.ForeignKey("PleasantHabit", on_delete=models.CASCADE, null=True, blank=True)
    frequency = models.CharField(choices=HabitFrequency.choices, default=HabitFrequency.Daily)
    award = models.CharField(max_length=100, null=False, blank=False, verbose_name="award for habit")
    duration = models.CharField(max_length=100, null=False, blank=False, verbose_name="habit duration")
    is_public = models.BooleanField(default=True)


class PleasantHabit:
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name="place for habit")
