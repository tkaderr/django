from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^secrets$', views.secrets),
    url(r'^postsecrets$', views.postsecrets),
    url(r'^popsecrets$', views.popsecrets),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^loggout$', views.loggout),
    url(r'^likes/(?P<id>\d+)$', views.likes)
]
