from django.db import models


# Create your models here.
class User(models.Model):
    name = models.TextField()
    status = models.TextField()

    class Meta:
        ordering = ['id']


class Location(models.Model):
    name = models.TextField()
    review = models.TextField()
    type = models.TextField()

    class Meta:
        ordering = ['id']


class Establishment(models.Model):
    name = models.TextField()
    review = models.FloatField()
    type = models.TextField()
    about = models.TextField()
    phone = models.TextField()
    address = models.TextField()

    class Meta:
        ordering = ['id']
