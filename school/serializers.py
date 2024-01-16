from rest_framework import serializers
from .models import Student, FirstClassRoom, SecondClassRoom, LastClassRoom

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

        extra_kwargs = {
            'approval_status' : {'read_only' : True},
        }


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


class First_Class_Room_Serializer(serializers.ModelSerializer):
    pass
    students = serializers.SerializerMethodField()
    class Meta:
        model = FirstClassRoom
        fields = [ 'room', 'school_year', 'students']
        
    def get_students(self, obj):
        return [student.name for student in obj.students.all()]


class Second_Class_Room_Serializer(serializers.ModelSerializer):
    students = serializers.SerializerMethodField()
    class Meta:
        model = SecondClassRoom
        fields = [ 'room', 'school_year','students']
    def get_students(self, obj):
        return [student.name for student in obj.students.all()]


class Last_Class_Room_Serializer(serializers.ModelSerializer):
    students = serializers.SerializerMethodField()
    class Meta:
        model = LastClassRoom
        fields = [ 'room', 'school_year','students']
    def get_students(self, obj):
        return [student.name for student in obj.students.all()]