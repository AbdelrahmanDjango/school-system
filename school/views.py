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
from django.db.models import Prefetch, Case, When, Value, CharField

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
    def list(self, request, *args, **kwargs):
     room_names = ['Operating System', 'Data Structures', 'Design Patterns', 'C++']

     data = {}
     for room_name in room_names:
        students_in_room = Student.objects.filter(first_class_rooms__room=room_name)
        serialized_students = [student.name for student in students_in_room]
        data[f'{room_name} Students'] = serialized_students

     return Response(data, status=status.HTTP_200_OK)


class Second_class_room_view(generics.ListAPIView):
    serializer_class = Second_Class_Room_Serializer
    def list(self, request, *args, **kwargs):
     room_names = ['OOP', 'Data Structures', 'Python', 'Network']

     data = {}
     for room_name in room_names:
        students_in_room = Student.objects.filter(first_class_rooms__room=room_name)
        serialized_students = [student.name for student in students_in_room]
        data[f'{room_name} Students'] = serialized_students

     return Response(data, status=status.HTTP_200_OK)



class Last_class_room_view(generics.ListAPIView):
    serializer_class = Last_Class_Room_Serializer
    def list(self, request, *args, **kwargs):
     room_names = ['Java Script', 'Websockets', 'Database', 'UI-UX']

     data = {}
     for room_name in room_names:
        students_in_room = Student.objects.filter(first_class_rooms__room=room_name)
        serialized_students = [student.name for student in students_in_room]
        data[f'{room_name} Students'] = serialized_students

     return Response(data, status=status.HTTP_200_OK)

    
