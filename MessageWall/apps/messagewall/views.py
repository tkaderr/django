from django.shortcuts import render, redirect, HttpResponse
from .models import User, Message
from django.contrib import messages
from django.core.urlresolvers import reverse
import bcrypt

def index(request):
    return render(request, "index.html")

def wall(request):
    context = {
    "user" : User.objects.get(id = request.session['uid']),
    "msgs" : Message.objects.all()
    }
    return render(request, "wall.html", context)

def mywall(request, id):
    context = {
    "user" : User.objects.get(id = id),
    "msgs" : Message.objects.all()
    }
    return render(request, "userwall.html", context)

def postmessage(request):
    user = User.objects.get(id = request.session['uid'])
    message = request.POST['message']
    Message.objects.create(content = message, user = user)
    return redirect('/wall')

def like(request, id):
    msg = Message.objects.get(id = id)
    user = User.objects.get(id = request.session['uid'])
    msg.likes.add(user)
    return redirect('/wall')

def favmsg(request, id):
    msg = Message.objects.get(id = id)
    user = User.objects.get(id = request.session['uid'])
    msg.faves.add(user)
    return redirect('/wall')

def register(request):
    request.session['login'] = False
    print request.session['login']
    fname = str(request.POST['first_name'])
    lname = str(request.POST['last_name'])
    email = str(request.POST['email'])
    pwd = request.POST['password'].encode()
    conpwd = request.POST['confirm_password'].encode()
    context = {
    "fname" : fname,
    "lname" : lname,
    "email" : email,
    "pwd" : pwd,
    "conpwd" : conpwd
    }
    if  User.objects.all().filter(email = email):
        messages.add_message(request, messages.INFO, "Email already exists! Please login")
        return redirect('/')
    error = User.objects.validate(context)
    if error:
        for ele in error:
            messages.add_message(request, messages.ERROR, ele)
        return redirect('/')
    else:
        hashedpwd = bcrypt.hashpw(pwd, bcrypt.gensalt())
        user = User.objects.create(first_name = fname, last_name = lname, email = email, password = hashedpwd)
        request.session['uid'] = user.id
        return redirect('/wall')

def login(request):
    request.session['login'] = True
    print request.session['login']
    email = str(request.POST['email'])
    pwd = request.POST['password'].encode()
    user = User.objects.all().filter(email = email)
    if  not user:
        messages.add_message(request, messages.INFO, "Email doesn't exist! Please register")
        return redirect('/')
    else:
        if user[0].password != bcrypt.hashpw(pwd, (user[0].password).encode()):
            messages.add_message(request, messages.INFO, "Invalid password")
            return redirect('/')
        else:
            request.session['uid'] = user[0].id
            return redirect('/wall')

def logout(request):
    request.session.clear()
    return redirect('/')
