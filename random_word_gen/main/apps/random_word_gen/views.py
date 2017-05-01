from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, "random_word_gen/index.html")

def result(request):
    return render(request, "random_word_gen/submitted.html")

def submitted(request):
    if not session["counter"]:
        request.session["counter"]=1
    if request.method == "POST":
        request.session["first_name"]=request.POST["first_name"]
        request.session["last_name"]=request.POST["last_name"]
        request.session["location"]=request.POST["location"]
        request.session["language"]=request.POST["language"]
        request.session["comments"]=request.POST["comments"]
        request.session["counter"]+=request.session["counter"]
        return redirect('/result')


# Create your views here.
