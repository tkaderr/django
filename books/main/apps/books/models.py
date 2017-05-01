from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=225)
    author=models.CharField(max_length=225)
    published_date=models.DateField(auto_now_add=True)
    category=models.CharField(max_length=225)
    in_print=models.BooleanField()
