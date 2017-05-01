from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, "landscape/index.html")

# def image(request):
#     return render(request, "landscape/image.html")


def process(request, number):
    print number
    context={
        "number":number
    }
    return render(request, "landscape/image.html", context)

# def process(request, num):
#     if num>=1 and num<=10:
#         request.session["image"]=1
#         return redirect('/image')
#     elif num >10 and num<=20:
#         request.session["image"]=2
#         return redirect('/image')
#     elif num >20 and num<=30:
#         request.session["image"]=3
#         return redirect('/image')
#     elif num >30 and num<=40:
#         request.session["image"]=4
#         return redirect('/image')
#     elif num >40 and num<=50:
#         request.session["image"]=5
#         return redirect('/image')
#     return redirect('/')
