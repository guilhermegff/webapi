from django.db import models


# Create your models here.
class User(models.Model):
    name = models.TextField()
    status = models.TextField()

    class Meta:
        ordering = ['id']


class Location(models.Model):
    #id = models.IntegerField(primary_key=True)
    name = models.TextField()
    review = models.TextField()
    type = models.TextField()

    class Meta:
        ordering = ['id']
