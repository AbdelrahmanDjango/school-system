from django.shortcuts import render, redirect
from . models import Student, FirstClassRoom, SecondClassRoom, LastClassRoom
from . serializers import (
      First_class_serializer,
       Second_class_serializer,
        Last_class_serializer,
         StudentSerializer, 
          First_Class_Room_Serializer,
           Second_Class_Room_Serializer,
            Last_Class_Room_Serializer,
              )
from rest_framework import generics, permissions, status, viewsets
from rest_framework.response import Response
from rest_framework import filters
from rest_framework.permissions import IsAdminUser
from django.db.models import Prefetch, Case, When, Value, CharField

class CreateStudent(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'address']
    permission_classes = [IsAdminUser]
    def get_queryset(self):
       return Student.objects.filter(approval_status=Student.Status.APPROVED)
    

# ______________________________________________________________ #

class First_class_view(generics.ListAPIView):
    serializer_class = First_class_serializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'address']
    def get_queryset(self):
       return Student.objects.filter(approval_status=Student.Status.APPROVED , school_year = 'First_class')



class Second_class_view(generics.ListAPIView):
    serializer_class = Second_class_serializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'address']
    def get_queryset(self):
       return Student.objects.filter(approval_status=Student.Status.APPROVED , school_year = 'Second_class')


class Last_class_view(generics.ListAPIView):
    serializer_class = Last_class_serializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'address']
    def get_queryset(self):
       return Student.objects.filter(approval_status=Student.Status.APPROVED , school_year = 'Last_class')

# ______________________________________________________________ #
    
class First_class_room_view(generics.ListAPIView):
    serializer_class = First_Class_Room_Serializer
    def list(self, request, *args, **kwargs):
     room_names = ['Operating System', 'Data Structures', 'Design Patterns', 'C++']

     data = {}
     for room_name in room_names:
        students_in_room = Student.objects.filter(first_class_rooms__room=room_name, approval_status=FirstClassRoom.Status.APPROVED)
        serialized_students = [student.name for student in students_in_room]
        data[f'{room_name} Students'] = serialized_students

     return Response(data, status=status.HTTP_200_OK)
    
    


class Second_class_room_view(generics.ListAPIView):
    serializer_class = Second_Class_Room_Serializer
    def list(self, request, *args, **kwargs):
     room_names = ['OOP', 'Data Structures', 'Python', 'Network']

     data = {}
     for room_name in room_names:
        students_in_room = Student.objects.filter(first_class_rooms__room=room_name, approval_status=SecondClassRoom.Status.APPROVED)
        serialized_students = [student.name for student in students_in_room]
        data[f'{room_name} Students'] = serialized_students

     return Response(data, status=status.HTTP_200_OK)



class Last_class_room_view(generics.ListAPIView):
    serializer_class = Last_Class_Room_Serializer
    def list(self, request, *args, **kwargs):
     room_names = ['Java Script', 'Websockets', 'Database', 'UI-UX']

     data = {}
     for room_name in room_names:
        students_in_room = Student.objects.filter(first_class_rooms__room=room_name, approval_status=LastClassRoom.Status.APPROVED)
        serialized_students = [student.name for student in students_in_room]
        data[f'{room_name} Students'] = serialized_students

     return Response(data, status=status.HTTP_200_OK)

