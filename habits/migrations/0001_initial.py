# Generated by Django 4.2.3 on 2023-08-07 18:27

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=100, verbose_name='place for habit')),
                ('time', models.TimeField(default=django.utils.timezone.now, verbose_name='start time for habit')),
                ('action', models.CharField(max_length=100, verbose_name='habit action')),
                ('is_pleasant', models.BooleanField(default=False, verbose_name='flag for pleasant habit')),
                ('frequency', models.CharField(choices=[('DAILY', 'Daily'), ('MONDAY', 'Monday'), ('TUESDAY', 'Tuesday'), ('WEDNESDAY', 'Wednesday'), ('THURSDAY', 'Thursday'), ('FRIDAY', 'Friday'), ('SATURDAY', 'Saturday'), ('SUNDAY', 'Sunday')], default='DAILY')),
                ('award', models.CharField(blank=True, max_length=100, null=True, verbose_name='award for habit')),
                ('duration', models.IntegerField(verbose_name='habit duration')),
                ('is_public', models.BooleanField(default=True)),
                ('link_pleasant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='habits.habit')),
            ],
            options={
                'verbose_name': 'habit',
                'verbose_name_plural': 'habits',
            },
        ),
    ]
