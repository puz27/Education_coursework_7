# Generated by Django 4.2.3 on 2023-08-07 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_users_chat_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='telegram_user_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
