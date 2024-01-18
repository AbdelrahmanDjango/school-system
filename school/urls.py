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
from rest_framework_nested import routers

app_name = 'school'

router = routers.SimpleRouter()
router.register('students/first_class', First_class_view, basename='first_class')

router2 = routers.SimpleRouter()
router2.register('students/second_class', Second_class_view, basename='second_class')

router3 = routers.SimpleRouter()
router3.register('students/last_class', Last_class_view, basename='last_class')

urlpatterns = [
    path('students/', CreateStudent.as_view(), name='create_student'),
    path('', include(router.urls)),
    path('', include(router2.urls)),
    path('', include(router3.urls)),


    path('rooms/first_class/', First_class_room_view.as_view(), name='first_class_room'),
    path('rooms/second_class/', Second_class_room_view.as_view(), name='second_class_room'),
    path('rooms/last_class/', Last_class_room_view.as_view(), name='last_class_room'),
]