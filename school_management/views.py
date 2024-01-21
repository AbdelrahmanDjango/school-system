from django.shortcuts import render, redirect
from school.models import (Student, FirstClassRoom, SecondClassRoom, LastClassRoom)
from .serializers import (StudentsRequestsSerializer,
                          FirstClassSerializer,
                          SecondClassSerializer,
                          LastClassSerializer, 
                          FirstClassRoomSerializer, 
                          SecondClassRoomSerializer, 
                          LastClassRoomSerializer)
from rest_framework import generics, permissions, status, viewsets
from rest_framework.response import Response
from rest_framework import filters
from rest_framework.permissions import IsAdminUser
from django.db.models import Prefetch, Case, When, Value, CharField
from rest_framework.exceptions import MethodNotAllowed



class StudentsRequestsView(viewsets.ModelViewSet):
   serializer_class = StudentsRequestsSerializer
   queryset = Student.objects.filter(approval_status=Student.Status.PENDING)
   permission_classes = [IsAdminUser]
      
class FirstClassView(viewsets.ModelViewSet):
    serializer_class = FirstClassSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'address']
    permission_classes = [IsAdminUser]
    def get_queryset(self):
      return Student.objects.filter(approval_status=Student.Status.APPROVED , school_year = 'First_class')
    def create(self, request, *args, **kwargs):
      if request.method == 'POST':
        raise MethodNotAllowed('POST')
      else:
        return super().create(request, *args, **kwargs)



class SecondClassView(viewsets.ModelViewSet):
    serializer_class = SecondClassSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'address']
    permission_classes = [IsAdminUser]
    def get_queryset(self):
       return Student.objects.filter(approval_status=Student.Status.APPROVED , school_year = 'Second_class')
    def create(self, request, *args, **kwargs):
      if request.method == 'POST':
        raise MethodNotAllowed('POST')
      else:
        return super().create(request, *args, **kwargs)


class LastClassView(viewsets.ModelViewSet):
    serializer_class = LastClassSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'address']
    permission_classes = [IsAdminUser]
    def get_queryset(self):
       return Student.objects.filter(approval_status=Student.Status.APPROVED , school_year = 'Last_class')
    def create(self, request, *args, **kwargs):
      if request.method == 'POST':
        raise MethodNotAllowed('POST')
      else:
        return super().create(request, *args, **kwargs)
      

class FirstClassRoomView(viewsets.ModelViewSet):
    serializer_class = FirstClassRoomSerializer
    queryset = FirstClassRoom.objects.filter(approval_status=FirstClassRoom.Status.PENDING)
    
    permission_classes = [IsAdminUser]
    def create(self, request, *args, **kwargs):
      if request.method == 'POST':
        raise MethodNotAllowed('POST')
      else:
        return super().create(request, *args, **kwargs)

    
    


class SecondClassRoomView(viewsets.ModelViewSet):
    serializer_class = SecondClassRoomSerializer
    permission_classes = [IsAdminUser]
    queryset = SecondClassRoom.objects.filter(approval_status=SecondClassRoom.Status.PENDING)

    def create(self, request, *args, **kwargs):
      if request.method == 'POST':
        raise MethodNotAllowed('POST')
      else:
        return super().create(request, *args, **kwargs)


class LastClassRoomView(viewsets.ModelViewSet):
    serializer_class = LastClassRoomSerializer
    queryset = LastClassRoom.objects.filter(approval_status=LastClassRoom.Status.PENDING)
    permission_classes = [IsAdminUser]

      
    def create(self, request, *args, **kwargs):
      if request.method == 'POST':
        raise MethodNotAllowed('POST')
      else:
        return super().create(request, *args, **kwargs)