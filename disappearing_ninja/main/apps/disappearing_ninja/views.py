from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"disappearing_ninja/index.html")

def ninja(request):
    return render(request, "disappearing_ninja/ninjas.html")

def ninja_turtle(request, color):
    context={
        "color":color
    }
    return render(request, "disappearing_ninja/ninja_color.html", context)
