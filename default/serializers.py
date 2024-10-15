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
        fields = ['id', 'attribute', 'gif']

class CourseSerializer(serializers.ModelSerializer):
    teachers = TeacherSerializer(many=True, read_only=True)
    attributes = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id', 'title', 'slug', 'video', 'description', 'about', 'attributes', 'teachers', 'last_update']

    def get_attributes(self, obj):
        attributes = CourseAttributes.objects.filter(course=obj).order_by('id')
        return CourseAttributesSerializer(attributes, many=True).data

class PreregSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prereg
        fields = ['name', 'phone', 'email', 'course']

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ['ip']