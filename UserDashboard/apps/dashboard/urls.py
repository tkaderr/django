from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^signin$', views.signin),
    url(r'^dashboard$', views.dashboard),
    url(r'^users/new$', views.newuser),
    url(r'^addnewuser$', views.addnewuser),
    url(r'^remove/(?P<id>\d+)$', views.removeuser),
    url(r'^users/show/(?P<id>\d+)$', views.showuser, name = "showuser"),
    url(r'^logout$', views.logout),
    url(r'^post/(?P<id>\d+)$', views.post),
    url(r'^postcomment/(?P<id>\d+)/(?P<userid>\d+)$', views.postcomment),
]
