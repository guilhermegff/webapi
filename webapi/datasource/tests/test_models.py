from django.test import TestCase
from rest_framework import status
from django.test import TestCase
from webapi.datasource.models import User


# Create your tests here.
class FirstTest(TestCase):
    def setUp(self):
        User.objects.create(name='Bob', status='offline')

    def test_user_name(self):
        user_bob = User.objects.get(name='Bob')
        self.assert_(user_bob.name, "Name is Bob")