from rest_framework import status
from django.test import TestCase
from ..models import User


# Create your tests here.
class FirstTest(TestCase):
    def setUp(self):
        User.objects.create(name='Bob', status='offline')

    def test_user_name(self):
        user_bob = User.objects.get(name='Bob')
        self.assertTrue(user_bob.name == "Bob", f"{user_bob.name} is not Bob")
