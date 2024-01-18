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

# _________________________________________________________________________________________________________#

class First_Class_Room_Serializer(serializers.ModelSerializer):
    students = serializers.SerializerMethodField()
    class Meta:
        model = FirstClassRoom
        fields = [ 'room', 'school_year', 'students']
        
    def get_students(self, obj):
        return [student.name for student in obj.students.all()]
    def get_students_by_room(self, room_name):
        students_in_room = Student.objects.filter(first_class_rooms__room=room_name, first_class_rooms__approval_status=FirstClassRoom.Status.APPROVED)
        return [student.name for student in students_in_room]


class Second_Class_Room_Serializer(serializers.ModelSerializer):
    students = serializers.SerializerMethodField()
    class Meta:
        model = SecondClassRoom
        fields = [ 'room', 'school_year','students']
    def get_students(self, obj):
        return [student.name for student in obj.students.all()]
    def get_students_by_room(self, room_name):
        students_in_room = Student.objects.filter(second_class_rooms__room=room_name, second_class_rooms__approval_status=SecondClassRoom.Status.APPROVED)
        return [student.name for student in students_in_room]


class Last_Class_Room_Serializer(serializers.ModelSerializer):
    students = serializers.SerializerMethodField()
    class Meta:
        model = LastClassRoom
        fields = [ 'room', 'school_year','students']
    def get_students(self, obj):
        return [student.name for student in obj.students.all()]
    def get_students_by_room(self, room_name):
        students_in_room = Student.objects.filter(last_class_rooms__room=room_name, last_class_rooms__approval_status=LastClassRoom.Status.APPROVED)
        return [student.name for student in students_in_room]