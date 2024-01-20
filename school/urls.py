from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (  FirstClassView,
                      SecondClassView,
                      LastClassView,
                      CreateStudent,
                      FirstClassRoomView,
                      SecondClassRoomView,
                      LastClassRoomView, 
                      
 )
from rest_framework_nested import routers

app_name = 'school'

router = routers.SimpleRouter()
router.register('students/first_class', FirstClassView, basename='first_class')

router2 = routers.SimpleRouter()
router2.register('students/second_class', SecondClassView, basename='second_class')

router3 = routers.SimpleRouter()
router3.register('students/last_class', LastClassView, basename='last_class')

urlpatterns = [
    path('students/', CreateStudent.as_view(), name='create_student'),
    path('', include(router.urls)),
    path('', include(router2.urls)),
    path('', include(router3.urls)),


    path('rooms/first_class/', FirstClassRoomView.as_view(), name='first_class_room'),
    path('rooms/second_class/', SecondClassRoomView.as_view(), name='second_class_room'),
    path('rooms/last_class/', LastClassRoomView.as_view(), name='last_class_room'),
]