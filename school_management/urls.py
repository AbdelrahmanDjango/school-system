from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (StudentsRequestsView,
                    FirstClassView,
                    SecondClassView,
                    LastClassView)
from rest_framework_nested import routers
app_name = 'school_management'

router1 = routers.SimpleRouter()
router1.register('management/students_requests', StudentsRequestsView)

router2 = routers.SimpleRouter()
router2.register('management/students/first_class', FirstClassView, basename='first_class')

router3 = routers.SimpleRouter()
router3.register('management/students/second_class', SecondClassView, basename='second_class')

router4 = routers.SimpleRouter()
router4.register('management/students/last_class', LastClassView, basename='last_class')



urlpatterns = [
    path('', include(router1.urls)),
    path('', include(router2.urls)),
    path('', include(router3.urls)),
    path('', include(router4.urls)),
]
