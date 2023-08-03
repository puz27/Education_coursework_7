from rest_framework.test import APITestCase
from habits.models import Habit
from rest_framework import status
from users.models import Users


class HabitTestCase(APITestCase):

    def setUp(self):
        """ Prepare testing """
        self.user = Users(email="test@gmail.com")
        self.user.set_password("test")
        self.user.save()

        response = self.client.post(
            "/api/v1/users/token/",
            {"email": "test@gmail.com", "password": "test"}
        )

        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")

        self.course = Users.objects.create(
            title="Test Course",
            description="Test Course description",
        )

        self.lesson = Users.objects.create(
            title="Test Lesson",
            description="Test Lesson description",
            course=self.course
        )

    def test_create_subscription(self):
        data = {'id': 1,
                'is_subscribed': False,
                "owner": 1,
                "course": 1
                }

        response = self.client.post("/api/v1/subscription/create/", data)
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertTrue(Subscription.objects.all().exists())

    def test_get_subscriptions(self):
        response = self.client.get("/api/v1/subscription/")

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_get_lessons(self):
            response = self.client.get("/api/v1/lesson/")

            self.assertEqual(
                response.status_code,
                status.HTTP_200_OK
            )

    def test_validate_lesson(self):
        data = {"title": "Test Lesson23",
                "description": "https://vk.com"
                }

        response = self.client.post("/api/v1/lesson/create/", data)

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_get_courses(self):
            response = self.client.get("/api/v1/course/")

            self.assertEqual(
                response.status_code,
                status.HTTP_200_OK
            )

    def test_validate_course(self):
            data = {"title": "Test Lesson23",
                    "description": "https://vk.com"
                    }

            response = self.client.post("/api/v1/course/create/", data)

            self.assertEqual(
                response.status_code,
                status.HTTP_400_BAD_REQUEST
            )
