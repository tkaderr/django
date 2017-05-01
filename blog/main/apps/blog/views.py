from django.shortcuts import render
from .models import Blog, Comment
# Create your views here.

def index(request):
    return "Hello"
