from __future__ import unicode_literals

from django.db import models


# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    email = models.CharField(max_length=225)
    password =  models.CharField(max_length=225)
    created_at= models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Comment(models.Model):
    user_id = models.ForeignKey(User)
    message_id = models.ForeignKey(Message)
    message=models.TextField()
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

class Message(models.Model)
    user_id=ManytoManyField(User, through = "User")
    message=TextField()
    created_at=DateField(auto_now_add=True)
    updated_at=DateField(auto_now=True)
