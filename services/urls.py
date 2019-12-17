
from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^$', GehaAllList.as_view(), name="services"),
    url(r'^single/(?P<pk>\d+)/$', OfficeRUD.as_view(), name="OfficeOneEdit"),
    url(r'^singleService/(?P<pk>\d+)/$', ServiceRUD.as_view(), name="ServiceOneEdit"),
    url(r'^ServiceAddon/RUD/(?P<pk>\d+)/$', ServiceAddonRUD.as_view(), name="ServiceAddonRUD"),
    url(r'^singleService/', CreateService.as_view(), name="ServiceCreate"),
    url(r'^ServiceAddon/create/', CreateServiceAddon.as_view(), name="ServiceAddonCreate"),
    url(r'^single/', CreateOffice.as_view(), name="OfficeCreate"),
    url(r'^office/(?P<pk>\d+)/$', OfficeList.as_view() , name='subservices'),
    url(r'^office/service/$', ServiceList.as_view() , name='subservices'),
    url(r'^parameters/$', ParametersList.as_view(), name='parameters'),
    url(r'^order/$', CreateOrder.as_view(), name='createOrder'),
]
