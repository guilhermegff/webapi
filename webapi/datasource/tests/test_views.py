import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import User
from ..serializers import UserSerializer

client = Client()


class GetAllUsersTest(TestCase):
    def setUp(self):
        User.objects.create(name="Bob", status='offline')
        User.objects.create(name="Alice", status='offline')
        User.objects.create(name="Smith", status='offline')

    def test_get_all_users(self):
        response = client.get(reverse("user_list"))
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


