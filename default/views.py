from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import NotFound
from .models import *
from .serializers import *

# Create your views here.
class CourseViewSet(ModelViewSet):
    http_method_names = ['get']
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'slug'  # Use slug instead of pk
    
    def get_object(self):
        queryset = self.get_queryset()
        slug = self.kwargs.get(self.lookup_field)
        try:
            return queryset.get(slug=slug)
        except Course.DoesNotExist:
            raise NotFound(f"Course with slug '{slug}' not found")

class CourseAttributesViewSet(ModelViewSet):
    http_method_names = ['get']
    serializer_class = CourseAttributesSerializer

    def get_queryset(self):
        return CourseAttributes.objects.filter(course__slug=self.kwargs['course_slug'])

    def get_serializer_context(self):
         return {'course_slug': self.kwargs['course_slug']}

class TeacherViewSet(ModelViewSet):
    http_method_names = ['get']
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class PreregViewSet(ModelViewSet):
    http_method_names = ['post']
    queryset = Prereg.objects.all()
    serializer_class = PreregSerializer

class LogViewSet(ModelViewSet):
    http_method_names = ['post']
    queryset = Log.objects.all()
    serializer_class = LogSerializer