# Generated by Django 4.2.3 on 2023-08-07 19:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0003_alter_habit_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='start time for habit'),
        ),
    ]
