from __future__ import unicode_literals

from django.db import models

class Client(models.Model):
    name= models.CharField(max_length=225)
    email= models.CharField(max_length=225)
    phone=models.CharField(max_length=225)
    note=models.TextField(max_length=225)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Project(models.Model):
    client=models.ForeignKey(Client, related_name="client_project")
    name=models.CharField(max_length=225)
    note=models.TextField(max_length=225)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
