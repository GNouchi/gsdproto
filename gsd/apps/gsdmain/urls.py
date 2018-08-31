# gsd main
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^logout', views.logout),
    url(r'^', views.main),
]