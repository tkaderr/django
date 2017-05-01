from django.shortcuts import render, redirect
import random
# Create your views here.

def index(request):
    return render(request,"surprise_me/index.html")


def results(request):
    return render(request, "surprise_me/results.html")

def process(request):
    values =["1", "2", "3", "4", "5"]
    x=[]
    random.shuffle(values)
    number=int(request.POST["action"])
    for i in range(0,number):
        x.append(values[i])
    request.session["vals"]=x
    print request.session["vals"]
    return redirect('/results')
