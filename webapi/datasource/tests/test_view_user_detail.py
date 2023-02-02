from rest_framework import status
from django.test import TestCase, Client
from django.test import TestCase, Client
from django.urls import reverse
from ..models import User
from ..serializers import UserSerializer

client = Client()


class GetSingleUserTest(TestCase):
    def setUp(self):
        self.bob = User.objects.create(name="Bob", status="offline")
        self.alice = User.objects.create(name="Alice", status="offline")
        self.smith = User.objects.create(name="Smith", status="offline")

    def test_get_valid_single_user(self):
        response = client.get(reverse("user_detail", kwargs={"pk": self.bob.pk}))
        print("value: {pk}".format(pk=self.bob.pk))
        user = User.objects.get(pk=self.bob.pk)
        serializer = UserSerializer(user)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_puppy(self):
        response = client.get(reverse("user_detail", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
