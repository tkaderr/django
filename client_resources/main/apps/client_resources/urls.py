from django.conf.urls import url, include
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^client/add$', views.addclientpage),
    url(r'^addclient$', views.addclient),
    url(r'^client/(?P<id>\d+)$', views.clientpage, name="show_client"),
    url(r'^addproject/(?P<id>\d+)$', views.addprojectpage),
    url(r'^addprojectprocess/(?P<id>\d+)$', views.addprojectprocess),
    url(r'^projectspage/(?P<id>\d+)$', views.projectspage, name="show_project")
]
