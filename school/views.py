from django.shortcuts import render, redirect
from . models import Student, FirstClassRoom, SecondClassRoom, LastClassRoom
from . serializers import (
      First_class_serializer,
       Second_class_serializer,
        Last_class_serializer,
         StudentSerializer, 
          First_Class_Room_Serializer,
           Second_Class_Room_Serializer,
            Last_Class_Room_Serializer )
from rest_framework import generics, permissions, status, viewsets
from rest_framework.response import Response
from rest_framework import filters
from rest_framework.permissions import IsAdminUser
# from django.http import status




class CreateStudent(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'address']
    permission_classes = [IsAdminUser]

# ______________________________________________________________ #

class First_class_view(generics.ListAPIView):
    serializer_class = First_class_serializer
    queryset = Student.objects.filter(school_year='First_class')
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'address']



class Second_class_view(generics.ListAPIView):
    serializer_class = Second_class_serializer
    queryset = Student.objects.filter(school_year='Second_class')
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'address']


class Last_class_view(generics.ListAPIView):
    serializer_class = Last_class_serializer
    queryset = Student.objects.filter(school_year='Last_class')
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'address']

# ______________________________________________________________ #
    
class First_class_room_view(generics.ListAPIView):
    serializer_class = First_Class_Room_Serializer
    queryset = FirstClassRoom.objects.all()

    
    
    


class Second_class_room_view(generics.ListAPIView):
    serializer_class = Second_Class_Room_Serializer
    queryset = SecondClassRoom.objects.all()


class Last_class_room_view(generics.ListAPIView):
    serializer_class = Last_Class_Room_Serializer
    queryset = LastClassRoom.objects.all()
