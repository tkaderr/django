from django.shortcuts import render
from .models import Book

# Create your views here.
def index(request):
    context={
        "books": Book.objects.all()
    }
    return "Hello"
