from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User


def index(request):
    return render(request, 'log_reg/index.html')

def success(request):
    return render(request, 'log_reg/success.html')

def login(request):
    email=request.POST["email"]
    password=request.POST["password"]
    login1={
        "email": email,
        "password": password
    }
    check=User.objects.validate_login(login1)
    if check:
        for i in range (0, len(check)):
            messages.add_message(request, messages.INFO, check[i])
        return redirect ('/')
    user1=User.objects.filter(email=email, password=password)
    for i in user1:
        request.session["first_name"]=i.first_name
        request.session["last_name"]=i.last_name
        request.session["email"]=i.email
    return redirect('/success')

def register(request):
    first_name=request.POST["first_name"]
    last_name=request.POST["last_name"]
    email=request.POST["email"]
    password=request.POST["password"]
    confirm_pw=request.POST["confirm_pw"]
    user1 = User.objects.filter(email = email)
    if user1:
        messages.add_message(request, messages.INFO, "Email exists, please login")
        return redirect ('/')
    register1 = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password,
        "confirm_pw": confirm_pw
    }
    check = User.objects.validate_registration(register1)
    if check:
        for x in range(0, len(check)):
            messages.add_message(request, messages.INFO, check[x])
        return redirect ('/')
    User.objects.create(first_name=first_name, last_name=last_name, email=email, password=password)
    user2 = User.objects.get(email=email, password=password)
    request.session["first_name"]=user2.first_name
    request.session["last_name"]=user2.last_name
    request.session["email"]=user2.email
    return redirect ('/success')

def loggout(request):
    request.session.clear()
    return redirect ('/')
