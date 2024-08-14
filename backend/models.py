from django.db import models

# Create your models here.
class People(models.Model):
    name = models.CharField(max_length=52)
    surname = models.CharField(max_length=52)
    age = models.IntegerField()