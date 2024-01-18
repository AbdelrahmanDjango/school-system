from rest_framework import serializers
from school.models import Student


class StudentsRequestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class First_class_serializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class Second_class_serializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class Last_class_serializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'