from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *

# Create your views here.
from rest_framework import viewsets

class CourseViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'slug'  # Use slug instead of pk

    def get_object(self):
        queryset = self.get_queryset()
        slug = self.kwargs.get(self.lookup_field)
        try:
            obj = queryset.get(slug=slug)
            obj.view_count += 1
            obj.save()
            return obj
        except Course.DoesNotExist:
            raise NotFound(f"Course '{slug}' not found")

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})
        return context

class CourseAttributesViewSet(ModelViewSet):
    http_method_names = ['get']
    serializer_class = CourseAttributeSerializer

    def get_queryset(self):
        return CourseAttributes.objects.filter(course__slug=self.kwargs['course_slug']).order_by('id')

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({
            'course_slug': self.kwargs['course_slug'],
            'request': self.request
        })
        return context

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