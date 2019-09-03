
from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^$', ServiceList.as_view(), name="services"),
    url(r'^subservices/(?P<pk>\d+)/$', SubServicesList.as_view() , name='subservices'),
    url(r'^parameters/(?P<pk>\d+)/$', ParametersList.as_view(), name='parameters'),
    url(r'^order/$', CreateOrder.as_view(), name='createOrder'),
]
