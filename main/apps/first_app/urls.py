from django.conf.urls import url
from . import views           # This line is new!



urlpatterns = [
    url(r'^$', views.index)     # This line has changed!
  ]


# from django.conf.urls import url, include
#
# def index(request):
#
# urlpatterns = [
#     url(r'^$', index)
# ]
