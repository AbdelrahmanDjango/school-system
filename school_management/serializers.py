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
    #students = serializers.PrimaryKeyRelatedField(queryset=Student.objects.filter(school_year='Second_class'), many=True)
    # student = serializers.SerializerMethodField()
    class Meta:
        model = FirstClassRoom
        # fields = '__all__'
        fields = ['id', 'room','approval_status', 'students']
    def get_student(self, obj):
        return obj.student.name



class SecondClassRoomSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SecondClassRoom
        fields = [ 'room', 'students']
        fields = ['id', 'room','approval_status', 'students']



class LastClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = LastClassRoom
        fields = ['id', 'room','approval_status', 'students']
