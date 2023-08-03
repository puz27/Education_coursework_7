from django.core.management import BaseCommand
from users.models import Users


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = Users.objects.create(
            email="admin@gmail.com",
            first_name="admin@gmail.com",
            last_name="admin@gmail.com",
            is_superuser=True,
            is_staff=True,
            is_active=True
            )

        user.set_password("admin")
        user.save()

        user = Users.objects.create(
            email="test1@gmail.com",
            first_name="test1@gmail.com",
            last_name="test1@gmail.com",
            is_superuser=False,
            is_staff=False,
            is_active=True
        )

        user.set_password("test")
        user.save()

        user = Users.objects.create(
            email="test2@gmail.com",
            first_name="test2@gmail.com",
            last_name="test2@gmail.com",
            is_superuser=False,
            is_staff=False,
            is_active=True
        )

        user.set_password("test2")
        user.save()

        user = Users.objects.create(
            email="test3@gmail.com",
            first_name="test3@gmail.com",
            last_name="test3@gmail.com",
            is_superuser=False,
            is_staff=False,
            is_active=True
        )

        user.set_password("test3")
        user.save()
