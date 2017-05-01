from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Blog(models.Model):
    title=models.CharField(max_length=225)
    author=models.CharField(max_length=225)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    blog=models.ForeignKey(Blog)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    
