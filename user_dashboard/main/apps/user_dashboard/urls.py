from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.welcome),
    url(r'^signin$', views.signin),
    url(r'^register$', views.register),
    url(r'^dashboard$', views.dashboard),
    url(r'^logout$', views.loggout)
]
