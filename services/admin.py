from django.contrib import admin
from .models import *
from django.core.exceptions import ValidationError


class GehaAdmin(admin.ModelAdmin):
    list_display = ('geha_id', 'geha_name', 'geha_icon')


class OfficeAdmin(admin.ModelAdmin):
    list_display = ('geha_id', 'off_id','off_name','off_icon')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('geha_id', 'off_id', 'srv_id' , 'srv_name', 'canBeOrdered', 'papers','actions')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('geha_id', 'ord_id', 'user_id',
                  'off_id', 'srv_id', 'ord_date' , 'ord_payment' ,'status')
    fields = ('status',)

class ServiceParameterAdmin(admin.ModelAdmin):
    list_display = ('parm_id','srv_id', 'parm_name' ,'is_rquired', 'parm_icon_name', 'param_type',
                  'conditions')
    fields = ('parm_id','srv_id', 'parm_name' ,'is_rquired', 'parm_icon_name', 'param_type',
                  'conditions' )

class ServiceParameterAnswerAdmin(admin.ModelAdmin):
    list_display = ('ans_id','ord_id', 'parm_id' ,'parm_name')


class DelivaryPlacesAdmin(admin.ModelAdmin):
    list_display = ('place_id','geha_id', 'place_name')
    




admin.site.register(Geha, GehaAdmin)
admin.site.register(Office, OfficeAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Order , OrderAdmin)
admin.site.register(ServiceParameter , ServiceParameterAdmin)
admin.site.register(ServiceParameterAnswer , ServiceParameterAnswerAdmin)
admin.site.register(DelivaryPlaces , DelivaryPlacesAdmin)
