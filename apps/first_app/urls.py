from django.conf.urls import url
from . import views  
from views import list         

urlpatterns = [
    url(r'^hi/$', views.index),
    url(r'^list/$', list, name='list'),
    url(r'^list/scan/$', views.scan),   
]