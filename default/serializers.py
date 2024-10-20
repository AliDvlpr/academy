from rest_framework import serializers
from .models import *

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['name', 'image', 'field', 'description']

class CourseAttributeSerializer(serializers.ModelSerializer):
    gif = serializers.SerializerMethodField()

    class Meta:
        model = CourseAttributes
        fields = ['id', 'attribute', 'gif']

    def get_gif(self, obj):
        request = self.context.get('request')
        gif_url = obj.gif.url if obj.gif else ''
        return request.build_absolute_uri(gif_url) if request else gif_url

    def create(self, validated_data):
        course_id = self.context['course_slug']
        return CourseAttributes.objects.create(course_id= course_id, **validated_data)

class GiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gift
        fields = ['title', 'description']
        
class CourseSerializer(serializers.ModelSerializer):
    teachers = TeacherSerializer(many=True, read_only=True)
    attributes = serializers.SerializerMethodField()
    gift = GiftSerializer(read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'title', 'slug', 'gift', 'roadmap', 'video', 'description', 'about', 'attributes', 'teachers', 'last_update']

    def get_attributes(self, obj):
        request = self.context.get('request')
        attributes = CourseAttributes.objects.filter(course=obj).order_by('id')
        serializer = CourseAttributeSerializer(attributes, many=True, context={'request': request})
        return serializer.data

class PreregSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prereg
        fields = ['name', 'phone', 'email', 'course']

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ['ip']