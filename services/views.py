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


class GehaList(generics.ListAPIView):
    queryset = Geha.objects.all()
    serializer_class = GehaSerializer
    permission_classes = (IsAuthenticated,) 


class OfficeList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk, format=None):
        offices = Office.objects.filter(geha_id_id = pk)
        serializer = OfficeSerializer(offices , many=True)
        return Response(serializer.data)


class ServiceList(generics.ListAPIView):
    serializer_class = ServiceSerializer
    permission_classes = (IsAuthenticated,) 
    def get_queryset(self):
        queryset = Service.objects.all()
        geha = self.request.query_params.get('geha')
        office = self.request.query_params.get('office')

        if geha:
            queryset = queryset.filter(geha_id_id=geha)
        elif office:
            office = queryset.filter(office_id_id=office)

        return queryset





class ParametersList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk, format=None):
        subServiceParameters = ServiceParameter.objects.filter(srv_id = pk)
        serializer = ServiceParameterSerializer(subServiceParameters , many=True)
        return Response(serializer.data)


class CreateOrder(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        user = request.user
        context = dict()
        if not self.request.user.active:
            return Response({"detail": "You are not active please contact MP system admin"}, status=status.HTTP_400_BAD_REQUEST)
        request.data['user'] = user.id
        serializer = OrderSerializer(
            data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        context['details'] = "Request submitted successfully!"
        return Response(context, status=status.HTTP_201_CREATED)