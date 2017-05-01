from __future__ import unicode_literals

from django.db import models

class People(models.Model):
    first_name=models.CharField(max_length=225)
    last_name=models.CharField(max_length=225)
    age=models.IntegerField()

    # def __str__(self):
    #     return self.first_name+ " " +self.last_name
