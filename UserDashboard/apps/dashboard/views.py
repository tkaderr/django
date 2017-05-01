from django.shortcuts import render, redirect, HttpResponse
from .models import User, Post, Comment
from django.contrib import messages
from django.db.models import Count
from django.core.urlresolvers import reverse
import bcrypt

def index(request):
    return render(request, "index.html")

def signin(request):
    return render(request, "logreg.html")

def dashboard(request):
    users = User.objects.all()
    curr_user = User.objects.get(id = request.session['uid'])
    context = {
    "users" : users,
    "curr_user" : curr_user
    }
    return render(request, "dashboard.html", context)

def newuser(request):
    return render(request, "newuser.html")

def addnewuser(request):
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
        return redirect('/users/new')
    error = User.objects.validate(context)
    if error:
        for ele in error:
            messages.add_message(request, messages.ERROR, ele)
        return redirect('/users/new')
    else:
        hashedpwd = bcrypt.hashpw(pwd, bcrypt.gensalt())
        if  not User.objects.all():
            ulevel = 9
        else:
            ulevel = 6
        user = User.objects.create(first_name = fname, last_name = lname, email = email, password = hashedpwd, user_level = ulevel)
        return redirect('/dashboard')

def showuser(request, id):
    loguser = User.objects.get(id = request.session['uid'])
    user = User.objects.get(id = id)
    posts = Post.objects.filter(user__id = id) #the user id clicked/users wall
    # posts = Post.objects.filter(user_comments__id = id)
    # comm = Comment.objects.filter(post = posts)
    comm = Comment.objects.all()
    context = {
    "user" : user,
    "posts": posts,
    "comments" : comm,
    "loguser" :loguser
    }
    return render(request, "showuser.html", context)

def removeuser(request, id):
    user = User.objects.get(id = id)
    user.delete()
    return redirect('/dashboard')

def post(request,id): # id of whom im posting
    post = request.POST['post']
    user = User.objects.get(id = id)
    uposted = User.objects.get(id = request.session['uid'])
    post = Post.objects.create(content = post, user = user, user_posted = uposted)
    return redirect(reverse('showuser', kwargs={'id': id }))

def postcomment(request, id, userid):
    comm = request.POST['comment']
    user = User.objects.get(id = request.session['uid'])
    post = Post.objects.get(id = id)
    comment = Comment.objects.create(content = comm, user = user, post = post)
    return redirect(reverse('showuser', kwargs={'id': userid })) # userid to get back to the users page

def register(request):
    request.session['login'] = False
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
    "conpwd" : conpwd,
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
        if  not User.objects.all():
            ulevel = 9
        else:
            ulevel = 6
        user = User.objects.create(first_name = fname, last_name = lname, email = email, password = hashedpwd, user_level = ulevel)
        request.session['uid'] = user.id
        return redirect('/dashboard')

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
            return redirect('/dashboard')

def logout(request):
    request.session.clear()
    return redirect('/')
