from django.shortcuts import render,redirect
import random
from time import strftime


new_game=True

def index(request):
    global new_game
    if new_game==True:
        request.session["gold"]=0
        request.session["log"]=[]
        new_game=False
    return render(request,"ninja_gold/index.html")

def process(request):
    if request.method=="POST":
        if request.POST["action"]=="farm":
            random_num=random.randint(10,20)
            request.session["gold"]=request.session["gold"]+random_num
            request.session["log"].insert(0,"You have earned "+str(random_num)+" gold"+str(strftime(" %Y-%m-%d %H:%M:%S")))
        elif request.POST["action"]=="cave":
            random_num=random.randint(5,10)
            request.session["gold"]=request.session["gold"]+random_num
            request.session["log"].insert(0,"You have earned "+str(random_num)+" gold"+str(strftime(" %Y-%m-%d %H:%M:%S")))
        elif request.POST["action"]=="house":
            random_num=random.randint(2,5)
            request.session["gold"]=request.session["gold"]+random_num
            request.session["log"].insert(0,"You have earned "+str(random_num)+" gold"+str(strftime(" %Y-%m-%d %H:%M:%S")))
        elif request.POST["action"]=="casino":
            random_num=random.randint(-50,50)
            request.session["gold"]=request.session["gold"]+random_num
            if random_num>=0:
                request.session["log"].insert(0,"You have earned "+str(random_num)+" gold"+str(strftime(" %Y-%m-%d %H:%M:%S")))
            else:
                request.session["log"].insert(0,"You have lost "+str(random_num)+" gold"+str(strftime(" %Y-%m-%d %H:%M:%S")))
    return redirect('/')

# def process(request):
#     if request.method=="POST":
#         if request.POST["action"]=="farm":
#             random_num=random.randint(10,20)
#             request.session["gold"]=request.session["gold"]+random_num
#             request.session["log"].append("You have earned "+str(random_num)+" gold"+str(strftime(" %Y-%m-%d %H:%M:%S")))
#         elif request.POST["action"]=="cave":
#             random_num=random.randint(5,10)
#             request.session["gold"]=request.session["gold"]+random_num
#             request.session["log"].append("You have earned "+str(random_num)+" gold"+str(strftime(" %Y-%m-%d %H:%M:%S")))
#         elif request.POST["action"]=="house":
#             random_num=random.randint(2,5)
#             request.session["gold"]=request.session["gold"]+random_num
#             request.session["log"].append("You have earned "+str(random_num)+" gold"+str(strftime(" %Y-%m-%d %H:%M:%S")))
#         elif request.POST["action"]=="casino":
#             random_num=random.randint(-50,50)
#             request.session["gold"]=request.session["gold"]+random_num
#             if random_num>=0:
#                 request.session["log"].append("You have earned "+str(random_num)+" gold"+str(strftime(" %Y-%m-%d %H:%M:%S")))
#             else:
#                 request.session["log"].append("You have lost "+str(random_num)+" gold"+str(strftime(" %Y-%m-%d %H:%M:%S")))
#     return redirect('/')
