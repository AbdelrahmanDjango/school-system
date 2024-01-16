from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (  First_class_view,
                      Second_class_view,
                      Last_class_view,
                      CreateStudent,
                      First_class_room_view,
                      Second_class_room_view,
                      Last_class_room_view, 
                      
 )

app_name = 'school'

urlpatterns = [
    path('students/', CreateStudent.as_view(), name='create_student'),
    path('students/first_class/', First_class_view.as_view(), name='first_class_list'),
    path('students/second_class/', Second_class_view.as_view(), name='second_class_list'),
    path('students/last_class/', Last_class_view.as_view(), name='last_class_list'),
    path('rooms/first_class/', First_class_room_view.as_view(), name='first_class_room'),
    path('rooms/second_class/', Second_class_room_view.as_view(), name='second_class_room'),
    path('rooms/last_class/', Last_class_room_view.as_view(), name='last_class_room'),
]