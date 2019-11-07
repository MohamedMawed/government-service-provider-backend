
from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^$', GehaAllList.as_view(), name="services"),
    url(r'^office/(?P<pk>\d+)/$', OfficeList.as_view() , name='subservices'),
    url(r'^office/service/$', ServiceList.as_view() , name='subservices'),
    url(r'^parameters/$', ParametersList.as_view(), name='parameters'),
    url(r'^order/$', CreateOrder.as_view(), name='createOrder'),
]
