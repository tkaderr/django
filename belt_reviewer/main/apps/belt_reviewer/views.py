from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Book, Review
from django.core.urlresolvers import reverse


def index(request):
    return render(request, 'belt_reviewer/index.html')

def books(request):
    context={
        "users": User.objects.get(id=request.session["id"]),
        "reviews": Review.objects.all().order_by('-created_at')[:3]
    }
    return render(request, 'belt_reviewer/books.html', context)

def add(request):
    context={
        "books":Book.objects.all()
    }
    return render(request, 'belt_reviewer/addreviews.html', context)

def bookreviews(request, id):
    book=Book.objects.get(id=id)
    context={
        "books": Book.objects.get(id=id),
        "reviews": Review.objects.filter(book=book)
    }
    return render(request, 'belt_reviewer/bookreviews.html', context)

def user(request, id):
    user =User.objects.get(id=id)
    context={
        "users": User.objects.get(id=id),
        "reviews": Review.objects.filter(user=user)
    }
    return render(request, 'belt_reviewer/user.html', context)

def home(request):
    return redirect('/books')

def addreviews(request):
    title=request.POST["title"]
    author=request.POST["author"]
    new_author=request.POST["new_author"]
    rating=request.POST["rating"]
    content=request.POST["comments"]
    author_query=Book.objects.filter(author=new_author)
    title_query=Book.objects.filter(title=title)
    if author_query:
        messages.add_message(request, messages.INFO, "Author exists, please user author dropdown")
        return redirect ('/add')
    if title_query:
        messages.add_message(request, messages.INFO, "title exists, please please find the book")
        return redirect ('/')
    if new_author:
        book1 = Book.objects.create(title=title, author=new_author)
    else:
        book1=Book.objects.create(title=title, author=author)
    user1=User.objects.get(id=request.session["id"])
    Review.objects.create(content=content, book=book1, user=user1, rating=rating )
    return redirect(reverse('show_book', kwargs={'id':book1.id}))

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
    return redirect('/books')

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
    return redirect ('/books')

def postreview(request, id):
    content=request.POST["comments"]
    rating=request.POST["rating"]
    book1 = Book.objects.get(id=id)
    user1=User.objects.get(id=request.session["id"])
    Review.objects.create(content=content, book=book1, user=user1, rating=rating )
    #return redirect('/bookreviews')
    return redirect(reverse('show_book', kwargs={'id':book1.id}))

def delete(request, id):
    review=Review.objects.get(id=id)
    book=Book.objects.get(book_review__id=id)
    review.delete()
    return redirect(reverse('show_book', kwargs={'id':book.id}))

def logout(request):
    request.session.clear()
    return redirect ('/')
