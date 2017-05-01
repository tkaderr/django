from django.shortcuts import render, redirect
from .models import User
import re
from django.contrib import messages
# Create your views here.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def index(request):
    return render(request, 'username_val/index.html')

def success(request):
    context={
        "success": User.objects.all()
    }
    return render(request, 'username_val/success.html', context)

def process(request):
    username=request.POST["username"]
    if len(username)<8 or len(username)>16 or not EMAIL_REGEX.match(username):
        messages.add_message(request, messages.INFO, 'Not Successful!')
        return redirect('/')
    User.objects.create(username=request.POST["username"])
    messages.add_message(request, messages.INFO, 'You successfully added {}!'.format(username))
    return redirect('/success')

def delete(request, id):
    delete1=User.objects.get(id=id)
    delete1.delete()
    return redirect('/success')
