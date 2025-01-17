from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name



class Role(models.Model):
    name = models.CharField(max_length=200)
    users = models.ManyToManyField(User, related_name='roles')

    def __str__(self):
        return self.name