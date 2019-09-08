from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import *

class GehaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geha
        fields = ('geha_id', 'geha_name', 'geha_icon')

class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = ('geha_id', 'off_id', 'off_name', 'off_icon')


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('geha_id', 'srv_id', 'off_id', 'srv_name',
                  'canBeOrdered', 'papers', 'actions')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('ord_id', 'user_id', 'srv_id', 'off_id', 'geha_id'
                  'ord_date', 'ord_payment', 'status')

    def get_user_id(self , obj):
        return obj.user_id.user_id

    def get_srv_id(self , obj):
        return obj.srv_id.srv_id

    def get_off_id(self , obj):
        return obj.off_id.off_id

class ServiceParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceParameter    
        fields = ('parm_id', 'srv_id', 'parm_icon_name', 'parm_name', 'is_rquired',
                  'param_type', 'conditions')    

    def get_srv_id(self , obj):
        return obj.srv_id.srv_id


class ServiceParameterAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceParameterAnswer    
        fields = ('ans_id', 'ord_id', 'parm_id', 'parm_name')    

    def get_srv_id(self , obj):
        return obj.parm_name

class DelivaryPlacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DelivaryPlaces    
        fields = ('place_id', 'geha_id', 'place_name')    

    def get_srv_id(self , obj):
        return obj.place_name

