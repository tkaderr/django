from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^secret$', views.secret),
    url(r'^logout$', views.logout),
    url(r'^addsecret$', views.addsecret),
    url(r'^addlike/(?P<id>\d+)$', views.addlike),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^mostpopular$', views.mostpopular)
]
