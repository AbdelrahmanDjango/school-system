from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (StudentsRequestsView,
                    First_class_view,
                    Second_class_view,
                    Last_class_view)
from rest_framework_nested import routers
app_name = 'school_management'

router = routers.SimpleRouter()
router.register('management/students_requests', StudentsRequestsView)

router = routers.SimpleRouter()
router.register('management/students/first_class', First_class_view, basename='first_class')

router2 = routers.SimpleRouter()
router2.register('management/students/second_class', Second_class_view, basename='second_class')

router3 = routers.SimpleRouter()
router3.register('management/students/last_class', Last_class_view, basename='last_class')



urlpatterns = [
    path('', include(router.urls)),
    path('', include(router.urls)),
    path('', include(router2.urls)),
    path('', include(router3.urls)),
]
