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
        ref_name = 'FirstClassSerializer'




class SecondClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        ref_name = 'SecondClassSerializer'


class LastClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        ref_name = 'LastClassSerializer'

class FirstClassRoomSerializer(serializers.ModelSerializer):
    student_name = serializers.SerializerMethodField()
    class Meta:
        model = FirstClassRoom
        fields = ['id', 'room','approval_status','student_name']
        ref_name = 'FirstClassRoomSerializer'
    def get_student_name(self, instance):
        first_student = instance.students.first()
        return first_student.name if first_student else None
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['students'] = [representation['student_name']]
        del representation['student_name']
        return representation






class SecondClassRoomSerializer(serializers.ModelSerializer):

    student_name = serializers.SerializerMethodField()
    

    class Meta:
        model = SecondClassRoom
        fields = [ 'room', 'students']
        fields = ['id', 'room','approval_status', 'students', 'student_name']
        ref_name = 'SecondClassRoomSerializer'
    def get_student_name(self, instance):
        first_student = instance.students.first()
        return first_student.name if first_student else None
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['students'] = [representation['student_name']]
        del representation['student_name']
        return representation



class LastClassRoomSerializer(serializers.ModelSerializer):

    student_name = serializers.SerializerMethodField()
    class Meta:
        model = LastClassRoom
        fields = ['id', 'room','approval_status', 'students', 'student_name']
        ref_name = 'LastClassRoomSerializer'
    def get_student_name(self, instance):
        first_student = instance.students.first()
        return first_student.name if first_student else None
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['students'] = [representation['student_name']]
        del representation['student_name']
        return representation
