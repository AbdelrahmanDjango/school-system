from rest_framework import serializers
from school.models import Student, FirstClassRoom, SecondClassRoom, LastClassRoom


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

class FirstClassRoomSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FirstClassRoom
        fields = '__all__'
        # fields = ['id', 'approval_status' ]

    # def get_students_by_room(self, room_name):
    #     students_in_room = Student.objects.filter(first_class_rooms__room=room_name, first_class_rooms__approval_status=FirstClassRoom.Status.APPROVED)
    #     return [student.name for student in students_in_room]


class SecondClassRoomSerializer(serializers.ModelSerializer):
    students = serializers.PrimaryKeyRelatedField(queryset=Student.objects.filter(school_year='Second_class'), many=True)
    
    class Meta:
        model = SecondClassRoom
        fields = [ 'room', 'students']

    def get_students_by_room(self, room_name):
        students_in_room = Student.objects.filter(second_class_rooms__room=room_name, second_class_rooms__approval_status=SecondClassRoom.Status.APPROVED)
        return [student.name for student in students_in_room]


class LastClassRoomSerializer(serializers.ModelSerializer):
    students = serializers.PrimaryKeyRelatedField(queryset=Student.objects.filter(school_year='Last_class'), many=True)
    class Meta:
        model = LastClassRoom
        fields = [ 'room', 'students']

    def get_students_by_room(self, room_name):
        students_in_room = Student.objects.filter(last_class_rooms__room=room_name, last_class_rooms__approval_status=LastClassRoom.Status.APPROVED)
        return [student.name for student in students_in_room]