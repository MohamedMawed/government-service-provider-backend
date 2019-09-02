from .models import *
from rest_framework.views import APIView
from .serializers import *
from accounts.serializers import UserSerializer
from accounts.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.core.exceptions import PermissionDenied
from rest_framework import status
# Create your views here.


class ServiceList(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = (IsAuthenticated,) 


class SubServicesList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk, format=None):
        if not self.request.user.active:
            return Response({"detail": "You are not active please contact MP system admin"}, status=status.HTTP_400_BAD_REQUEST)
        Subservices = SubService.objects.get(service = pk)
        serializer = SubServiceSerializer(Subservices)
        return Response(serializer.data)

class ParametersList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk, format=None):
        if not self.request.user.active:
            return Response({"detail": "You are not active please contact MP system admin"}, status=status.HTTP_400_BAD_REQUEST)
        SubServiceParameters = SubServiceParameter.objects.get(subService = pk)
        serializer = SubServiceSerializer(SubServiceParameters)
        return Response(serializer.data)