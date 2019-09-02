from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import *


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'name')


class SubServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubService
        fields = ('id', 'service', 'name', 'papers', 'actions')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'user', 'username', 'service', 'serviceName',
                  'subService', 'subServiceName', 'paymentType', 'status')
    def get_user(self , obj):
        return obj.user.username

    def get_service(self , obj):
        return obj.service.name

    def get_subService(self , obj):
        return obj.subService.name

class SubServiceParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubServiceParameter    
        fields = ('id', 'subService', 'subServiceName', 'paramName', 'isRequired',
                  'paramType', 'conditions')    
    def get_subService(self , obj):
        return obj.subService.name
