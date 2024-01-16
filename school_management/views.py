from django.shortcuts import render, redirect
from school.models import (Student)
from .serializers import (StudentsRequestsSerializer)
from rest_framework import generics, permissions, status, viewsets
from rest_framework.response import Response
from rest_framework import filters
from rest_framework.permissions import IsAdminUser
from django.db.models import Prefetch, Case, When, Value, CharField
from rest_framework.exceptions import MethodNotAllowed



class StudentsRequestsView(viewsets.ModelViewSet):
   serializer_class = StudentsRequestsSerializer
   queryset = Student.objects.all()
   permission_classes = [IsAdminUser]
   def create(self, request, *args, **kwargs):
      if request.method == 'POST':
       raise MethodNotAllowed('POST')
      else:
        return super().create(request, *args, **kwargs)
      