from rest_framework import serializers
from .models import *

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['name', 'image', 'field', 'description']

class CourseAttributesSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        course_id = self.context['product_id']
        return CourseAttributes.objects.create(course_id= course_id, **validated_data)
        
    class Meta:
        model = CourseAttributes
        fields = ['id', 'attribute']

class CourseSerializer(serializers.ModelSerializer):
    teachers = TeacherSerializer(many=True, read_only=True)
    attributes = CourseAttributesSerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields =  ['id','title','slug', 'video', 'description', 'about', 'attributes', 'teachers', 'last_update']


class PreregSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prereg
        fields = ['name', 'phone', 'email', 'course']

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ['ip']