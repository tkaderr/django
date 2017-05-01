from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "real_portfolio/index.html")

def about(request):
    return render(request, "real_portfolio/about.html")

def projects(request):
    return render(request, "real_portfolio/projects.html")

def testimonials(request):
    return render(request, "real_portfolio/testimonials.html")
