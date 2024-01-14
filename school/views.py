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
    def list(self, request, *args, **kwargs):
        # first_class_rooms = FirstClassRoom.objects.all()
        # serialized_rooms = self.serializer_class(first_class_rooms, many=True).data
        students_in_operating_system = Student.objects.filter(first_class_rooms__room='Operating System')
        students_in_data_structures = Student.objects.filter(first_class_rooms__room='Data Structures')
        students_in_design_patterns = Student.objects.filter(first_class_rooms__room='Design Patterns')
        students_in_CPP = Student.objects.filter(first_class_rooms__room='C++')

        serialized_operating_system_students = [student.name for student in students_in_operating_system]
        serialized_data_structures_students = [student.name for student in students_in_data_structures]
        serialized_design_patterns_students = [student.name for student in students_in_design_patterns]
        serialized_CPP_students = [student.name for student in students_in_CPP]

        data = {
            'Operating System Students': serialized_operating_system_students,
            'Data Structuers Students': serialized_data_structures_students,
            'Design Patterns Students': serialized_design_patterns_students,
            'C++ Students': serialized_CPP_students
        }

        return Response(data, status=status.HTTP_200_OK)

class Second_class_room_view(generics.ListAPIView):
    serializer_class = Second_Class_Room_Serializer
    def list(self, request, *args, **kwargs):
        students_in_OOP = Student.objects.filter(second_class_rooms__room='OOP')
        students_in_data_structures = Student.objects.filter(second_class_rooms__room='Data Structures')
        students_in_python = Student.objects.filter(second_class_rooms__room='Python')
        students_in_network = Student.objects.filter(second_class_rooms__room='Network')

        serialized_OOP_students = [student.name for student in students_in_OOP]
        serialized_data_structures_students = [student.name for student in students_in_data_structures]
        serialized_python_students = [student.name for student in students_in_python]
        serialized_network_students = [student.name for student in students_in_network]

        data = {
            'OOP Students': serialized_OOP_students,
            'Data Structuers Students': serialized_data_structures_students,
            'Python Students': serialized_python_students,
            'Network Students': serialized_network_students
        }

        return Response(data, status=status.HTTP_200_OK)


class Last_class_room_view(generics.ListAPIView):
    serializer_class = Last_Class_Room_Serializer
    def list(self, request, *args, **kwargs):
        students_in_java_script = Student.objects.filter(first_class_rooms__room='Java Script')
        students_in_websockets= Student.objects.filter(first_class_rooms__room='Websockets')
        students_in_database= Student.objects.filter(first_class_rooms__room='Database')
        students_in_UI_UX = Student.objects.filter(first_class_rooms__room='UI-UX')

        serialized_java_script_students = [student.name for student in students_in_java_script]
        serialized_webscokets_students = [student.name for student in students_in_websockets]
        serialized_database_students = [student.name for student in students_in_database]
        serialized_UI_UX_students = [student.name for student in students_in_UI_UX]

        data = {
            'Java Script Students': serialized_java_script_students,
            'Websockets Students': serialized_webscokets_students,
            'Database Students': serialized_database_students,
            'UI-UX Students': serialized_UI_UX_students
        }

        return Response(data, status=status.HTTP_200_OK)
