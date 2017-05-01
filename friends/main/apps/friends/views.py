from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt


def index(request):
    return render(request, 'friends/index.html')

def friends(request):
    context={
        "user": User.objects.get(id=request.session["id"])
    }
    return render(request, 'friends/friends.html', context)

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
    return redirect('/friends')

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
    user2=User.objects.create(first_name=first_name, last_name=last_name, email=email, password=password)
    request.session["id"]=user2.id
    return redirect ('/friends')

def addfriend(request):
    user=User.objects.get(id=request.session["id"])
    user1=User.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"])
    user.friends.add(user1)
    return redirect ('/friends')

def delete(request, id):
    user = User.objects.get(id = request.session['id'])
    user1 = User.objects.get(id = id)
    user.friends.remove(user1)
    # user1=User.objects.filter(id=request.session["id"], friends__id=id)
    # user1.delete()
    print "user",  user
    print "friend user", user1
    return redirect ('/friends')

def logout(request):
    request.session.clear()
    return redirect ('/')
