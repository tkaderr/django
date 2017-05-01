from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^wall$', views.wall),
    url(r'^postmessage$', views.postmessage),
    url(r'^like/(?P<id>\d+)$', views.like),
    url(r'^wall$', views.wall),
    url(r'^favmsg/(?P<id>\d+)$', views.favmsg),
    url(r'^mywall/(?P<id>\d+)$', views.mywall),
]
