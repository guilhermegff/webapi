from django.db import models


# Create your models here.
class User(models.Model):
    name = models.TextField()
    status = models.TextField()

    class Meta:
        ordering = ['id']
