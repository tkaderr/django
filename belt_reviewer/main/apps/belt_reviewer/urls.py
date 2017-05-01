from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^books$', views.books),
    url(r'^logout$', views.logout),
    url(r'^add$', views.add),
    url(r'^home$', views.home),
    url(r'^addreviews$', views.addreviews),
    url(r'^bookreviews/(?P<id>\d+)$', views.bookreviews, name="show_book"),
    url(r'^postreview/(?P<id>\d+)$', views.postreview),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^user/(?P<id>\d+)$', views.user)


]
