from django.db import models
from django.db.models.signals import post_save


class User(models.Model):
    username = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.last_name + self.first_name
