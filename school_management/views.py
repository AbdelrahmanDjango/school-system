from django.shortcuts import render, redirect
from school.models import (Student)
from .serializers import (StudentsRequestsSerializer,
                          FirstClassSerializer,
                          SecondClassSerializer,
                          LastClassSerializer)
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
      