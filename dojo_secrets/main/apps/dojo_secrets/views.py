from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Secret
from django.db.models import Count


def index(request):
    return render(request, 'dojo_secrets/index.html')

def secrets(request):
    context = {
        "users": User.objects.get(id = int(request.session['id'])),
        "secrets": Secret.objects.all().order_by('-created_at')
    }
    return render(request, 'dojo_secrets/secrets.html', context)

def popsecrets(request):
    context={
        "pop_secrets": Secret.objects.all()
    }
    return render(request, "dojo_secrets/popular_secrets.html", context)

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
    return redirect('/secrets')

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
    return redirect ('/secrets')

def postsecrets(request):
    user = User.objects.get(id=int(request.session['id']))
    comm = request.POST['sec']
    Secret.objects.create(comment=comm, users=user)
    return redirect ('/secrets')

def likes(request, id):
    this_user = User.objects.get(id=request.session['id'])
    this_secret = Secret.objects.get(id=id)
    this_secret.likes.add(this_user)
    return redirect ('/secrets')

def delete(request, id):
    delete1 = Secret.objects.get(id = id)
    delete1.delete()
    return redirect ('/secrets')

def loggout(request):
    request.session.clear()
    return redirect ('/')
