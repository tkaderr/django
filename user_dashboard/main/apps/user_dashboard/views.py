from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User


def welcome(request):
    return render(request, 'user_dashboard/welcome.html')

def signin(request):
    return render(request, 'user_dashboard/signin.html')

def dashboard(request):
    context={
        "users":User.objects.all()
    }
    return render(request, 'user_dashboard/success.html')

def messageboard(request, id):
    return render(request, 'user_dashboard/messageboard.html')

def updateuserinfo(request, id):
    return render(request, 'user_dashboard/edituser.html')

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
        return redirect ('/signin')
    user1=User.objects.filter(email=email, password=password)
    request.session["id"]=user1[0]
    return redirect('/dashboard')

def register(request):
    first_name=request.POST["first_name"]
    last_name=request.POST["last_name"]
    email=request.POST["email"]
    password=request.POST["password"]
    confirm_pw=request.POST["confirm_pw"]
    user1 = User.objects.filter(email = email)
    if user1:
        messages.add_message(request, messages.INFO, "Email exists, please login")
        return redirect ('/signin')
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
    request.session["id"]=user2.id
    return redirect ('/dashboard')

def logout(request):
    request.session.clear()
    return redirect ('/')
