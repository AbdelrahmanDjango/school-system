from rest_framework import serializers
from school.models import Student


class StudentsRequestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class FirstClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class SecondClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class LastClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'