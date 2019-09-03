from django.contrib import admin
from .models import *
from django.core.exceptions import ValidationError


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


class SubServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'service', 'name' , 'canBeOrdered', 'papers', 'actions')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'service',
                  'subService', 'paymentType', 'status' , 'requiredFieldsAnswers')
    fields = ( 'user', 'service',
                  'subService', 'paymentType', 'status' , 'requiredFieldsAnswers')

class SubServiceParameterAdmin(admin.ModelAdmin):
    list_display = ('id','subService', 'paramName' ,'iconName', 'isRequired', 'paramType',
                  'conditions')
    fields = ( 'subService' , 'paramName',
                  'isRequired','iconName', 'paramType', 'conditions')





admin.site.register(Service, ServiceAdmin)
admin.site.register(SubService, SubServiceAdmin)
admin.site.register(Order , OrderAdmin)
admin.site.register(SubServiceParameter , SubServiceParameterAdmin)
