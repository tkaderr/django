from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
import re


FIRST_NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
LAST_NAME_REGEX =re.compile(r'^[a-zA-Z]*$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validate_registration(self,data):
        arr=[]
        if len(data["first_name"])<2 or not FIRST_NAME_REGEX.match(data["first_name"]):
            arr.append("First Name has to be atleast 2 characters and no numbers")
        if len(data["last_name"])<2 or not LAST_NAME_REGEX.match(data["last_name"]):
            arr.append("Last Name has to be atleast 2 characters and no numbers")
        if not EMAIL_REGEX.match(data["email"]):
            arr.append("Email not valid!")
        if len(data["password"])<8:
            arr.append("Password has to be atleast 8 characters long")
        if data["password"]!=data["confirm_pw"]:
            arr.append("Password and Confirm Password do not match")
        return arr

    def validate_login(self, data):
        arr=[]
        u_email=User.objects.filter(email=data["email"])
        if not u_email:
            arr.append("Email does not exist")
        p_email=User.objects.filter(email=data["email"], password=data["password"])
        if not p_email:
            arr.append("Incorrect Password/Email")
        return arr



class User(models.Model):
    first_name=models.CharField(max_length=225)
    last_name=models.CharField(max_length=225)
    email=models.CharField(max_length=225)
    password=models.CharField(max_length=225)
    created_at=models.DateField(auto_now_add=True)
    objects=UserManager()
