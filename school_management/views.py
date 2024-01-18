from django.shortcuts import render, redirect
from school.models import (Student)
from .serializers import (StudentsRequestsSerializer,
                          First_class_serializer,
                          Second_class_serializer,
                          Last_class_serializer)
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
      
class First_class_view(viewsets.ModelViewSet):
    serializer_class = First_class_serializer
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



class Second_class_view(viewsets.ModelViewSet):
    serializer_class = Second_class_serializer
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


class Last_class_view(viewsets.ModelViewSet):
    serializer_class = Last_class_serializer
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
      