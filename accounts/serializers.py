from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import *
from django.core.files.base import ContentFile
import base64, uuid


class UserSerializer(serializers.ModelSerializer):
    mobile  = serializers.CharField(source='username', validators=[UniqueValidator(queryset=User.objects.all(), message="A user with that mobile number already exists")])

    class Meta:
        model   = User
        fields  = ('id', 'mobile', 'password', 'full_name', 'email', 'avatar' , 'address','government')

        extra_kwargs = {
            'password'  : {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def validate(self, attrs):
        """
        validation mobile number
        """
        if 'username' in attrs.keys():
            mobile_length = len(attrs['username'])
            if mobile_length > 15 or mobile_length < 9:
                raise serializers.ValidationError("This is invalid mobile number")
            for ch in attrs['username']:
                if ch < '0' or ch > '9':
                    raise serializers.ValidationError("Mobile number mustn't contains numbers only")
        return attrs



class ChangePasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            # base64 encoded image - decode
            format, imgstr = data.split(';base64,') # format ~= data:image/X,
            ext = format.split('/')[-1] # guess file extension
            id = uuid.uuid4()
            data = ContentFile(base64.b64decode(imgstr), name = id.urn[9:] + '.' + ext)
        return super(Base64ImageField, self).to_internal_value(data)