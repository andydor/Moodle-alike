from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100, default='null')
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100, default='null')

    def __str__(self):
        return self.last_name + self.first_name


