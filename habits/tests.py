from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken

from habits.models import Habit
from users.models import Users


class HabitTestCase(APITestCase):

    def setUp(self):
        """ Prepare testing """
        self.user = Users(
            email="test@gmail.com",
            is_superuser=False,
            is_staff=False,
            is_active=True,
            )

        self.user.set_password("test")
        self.user.save()

        self.client = APIClient()
        token = AccessToken.for_user(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    def test_create_habit(self):
        """ Create test habit """
        data = {
            "place": "At home.",
            "time": "14:00:00",
            "action": "Clean windows.",
            "is_pleasant": "False",
            "frequency": "SUNDAY",
            "award": "To drink bear.",
            "duration": 10,
            "is_public": "True",
            "owner": 1
            }

        response = self.client.post("/api/v1/habit/create/", data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Habit.objects.all().exists())

    def test_get_habit(self):
        """ Test all habits of owner or public """
        response = self.client.get("/api/v1/habits/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_habit(self):
        """ Test all habits of owner or public """
        response = self.client.get("/api/v1/habit/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    # def test_get_subscriptions(self):
    #     response = self.client.get("/api/v1/subscription/")
    #
    #     self.assertEqual(
    #         response.status_code,
    #         status.HTTP_200_OK
    #     )
    #
    # def test_get_lessons(self):
    #         response = self.client.get("/api/v1/lesson/")
    #
    #         self.assertEqual(
    #             response.status_code,
    #             status.HTTP_200_OK
    #         )
    #
    # def test_validate_lesson(self):
    #     data = {"title": "Test Lesson23",
    #             "description": "https://vk.com"
    #             }
    #
    #     response = self.client.post("/api/v1/lesson/create/", data)
    #
    #     self.assertEqual(
    #         response.status_code,
    #         status.HTTP_400_BAD_REQUEST
    #     )
    #
    # def test_get_courses(self):
    #         response = self.client.get("/api/v1/course/")
    #
    #         self.assertEqual(
    #             response.status_code,
    #             status.HTTP_200_OK
    #         )
    #
    # def test_validate_course(self):
    #         data = {"title": "Test Lesson23",
    #                 "description": "https://vk.com"
    #                 }
    #
    #         response = self.client.post("/api/v1/course/create/", data)
    #
    #         self.assertEqual(
    #             response.status_code,
    #             status.HTTP_400_BAD_REQUEST
    #         )
