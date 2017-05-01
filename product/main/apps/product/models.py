from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=255)
    description= models.TextField(max_length=None)
    weight= models.CharField(max_length=255)
    price= models.IntegerField(max_length=None)
    cost=models.IntegerField(max_length=None)
    category=models.CharField(max_length=255)
