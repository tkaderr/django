from django.shortcuts import render, redirect
from .models import Product
# Create your views here.

def index(request):
    context={
        "products": Product.objects.all()
    }
    return render(request, 'product/index.html', context)

def products(request):
    Product.objects.create(name=request.POST["name"], description=request.POST["description"], weight=request.POST["weight"], price=request.POST["price"], cost=request.POST["cost"], category=request.POST["category"])
    
    return redirect('/')
