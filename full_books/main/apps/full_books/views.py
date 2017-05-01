from django.shortcuts import render, redirect
from .models import Book

def index(request):
    context={
        "book": Book.objects.all()
    }
    return render(request, 'full_books/index.html', context)

def process(request):
    Book.objects.create(title=request.POST["title"], author=request.POST["author"], category=request.POST["category"])
    return redirect('/')
