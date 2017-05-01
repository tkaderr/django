from django.shortcuts import render
import time

# Create your views here.
def index(request):

    request.session['date']= time.asctime( time.localtime(time.time()) )
    return render(request, 'timedisplay/index.html')
