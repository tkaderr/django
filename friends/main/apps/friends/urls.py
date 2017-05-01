from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^friends$', views.friends),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^addfriend$', views.addfriend),
    url(r'^logout$', views.logout)
]
