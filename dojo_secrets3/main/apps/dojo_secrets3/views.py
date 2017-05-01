from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Secret
from django.db.models import Count


def index(request):
    return render(request, 'dojo_secrets3/index.html')

def secret(request):
    context={
        "users": User.objects.get(id=request.session["id"]),
        "secret": Secret.objects.all().order_by("-created_at")[:5]
    }
    return render(request, 'dojo_secrets3/secrets.html', context)

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
    request.session["id"]=user1[0].id
    return redirect('/secret')

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
    request.session["id"]=user2.id
    return redirect ('/secret')

def addsecret(request):
    user=User.objects.get(id=request.session["id"])
    Secret.objects.create(content=request.POST["message"], user=user)
    return redirect('/secret')

def addlike(request,id):
    user=User.objects.get(id=request.session["id"])
    secret=Secret.objects.get(id=id)
    secret.like.add(user)
    return redirect('/secret')

def delete(request,id):
    secret=Secret.objects.get(id=id)
    secret.delete()
    return redirect('/secret')

def mostpopular(request):
    context={
        "users": User.objects.get(id=request.session["id"]),
        "secret": Secret.objects.all().order_by("-created_at")
    }
    return render(request, 'dojo_secrets3/mostpopular.html', context)


def logout(request):
    request.session.clear()
    return redirect ('/')
