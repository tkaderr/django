from django.shortcuts import render, redirect
from .models import Client, Project
from django.core.urlresolvers import reverse

def index(request):
    context={
        "clients": Client.objects.all()
    }
    return render(request, 'index.html', context)

def addclientpage(request):
    return render(request, 'addclient.html')

def addclient(request):
    client=Client.objects.create(name = request.POST["client_name"], email = request.POST["client_email"], phone = request.POST["client_phone"], note = request.POST["client_notes"])
    return redirect(reverse('show_client', kwargs={'id':client.id}))

def clientpage(request, id):
    client=Client.objects.get(id=id)
    project=Project.objects.filter(client=client)
    context={
        "clients": client,
        "projects": project
    }
    return render(request, 'clientpage.html', context)

def addprojectpage(request,id):
    context={
        "clients":Client.objects.get(id=id)
    }
    return render(request, 'addproject.html', context)

def addprojectprocess(request,id):
    client=Client.objects.get(id=id)
    project=Project.objects.create(name=request.POST["name"], note=request.POST["notes"], client=client)
    return redirect(reverse('show_project', kwargs={'id':project.id}))

def projectspage(request, id):
    context={
        "projects": Project.objects.get(id=id)
    }
    return render(request, 'projects.html', context)
