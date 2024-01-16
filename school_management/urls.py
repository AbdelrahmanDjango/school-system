from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentsRequestsView
from rest_framework_nested import routers

router = routers.SimpleRouter()
router.register('students_requests', StudentsRequestsView)

app_name = 'school_management'


urlpatterns = [
    path('', include(router.urls)),
]
