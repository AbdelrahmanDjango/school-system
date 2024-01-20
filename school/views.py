from django.shortcuts import render, redirect
from . models import Student, FirstClassRoom, SecondClassRoom, LastClassRoom
from . serializers import (
      FirstClassSerializer,
       SecondClassSerializer,
        LastClassSerializer,
         StudentSerializer, 
          FirstClassRoomSerializer,
           SecondClassRoomSerializer,
            LastClassRoomSerializer,
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
    def get_queryset(self):
       return Student.objects.filter(approval_status=Student.Status.APPROVED)
    

# ______________________________________________________________ #

class FirstClassView(viewsets.ReadOnlyModelViewSet):
    serializer_class = FirstClassSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'address']
    def get_queryset(self):
       return Student.objects.filter(approval_status=Student.Status.APPROVED , school_year = 'First_class')



class SecondClassView(viewsets.ReadOnlyModelViewSet):
    serializer_class = SecondClassSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'address']
    def get_queryset(self):
       return Student.objects.filter(approval_status=Student.Status.APPROVED , school_year = 'Second_class')


class LastClassView(viewsets.ReadOnlyModelViewSet):
    serializer_class = LastClassSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'address']
    def get_queryset(self):
       return Student.objects.filter(approval_status=Student.Status.APPROVED , school_year = 'Last_class')

# ______________________________________________________________ #
    
class FirstClassRoomView(generics.ListCreateAPIView):
    serializer_class = FirstClassRoomSerializer
    def list(self, request, *args, **kwargs):

        room_names = ['Operating System', 'Data Structures', 'Design Patterns', 'C++']

        data = {}
        serializer = self.serializer_class()

        for room_name in room_names:
            serialized_students = serializer.get_students_by_room(room_name)
            data[f'{room_name} Students'] = serialized_students

        return Response(data, status=status.HTTP_200_OK)
    
    


class SecondClassRoomView(generics.ListCreateAPIView):
    serializer_class = SecondClassRoomSerializer

    def list(self, request, *args, **kwargs):
        room_names = ['OOP', 'Data Structures', 'Python', 'Network']

        data = {}
        serializer = self.get_serializer()

        for room_name in room_names:
            serialized_students = serializer.get_students_by_room(room_name)
            data[f'{room_name} Students'] = serialized_students

        return Response(data, status=status.HTTP_200_OK)



class LastClassRoomView(generics.ListCreateAPIView):
    serializer_class = LastClassRoomSerializer
    def list(self, request, *args, **kwargs):
        room_names = ['Java Script', 'Websockets', 'Database', 'UI-UX']

        data = {}
        serializer = self.get_serializer()

        for room_name in room_names:
            serialized_students = serializer.get_students_by_room(room_name)
            data[f'{room_name} Students'] = serialized_students

        return Response(data, status=status.HTTP_200_OK)

