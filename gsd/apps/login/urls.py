# gsd login
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login', views.login),
    url(r'^registration', views.registration),
    url(r'^landing', views.landing),
    url(r'^landing', views.landing),
]