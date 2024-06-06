from django.contrib import admin
from django.utils.html import format_html
from .models import *


class CourseAttributesInline(admin.TabularInline):
    model = CourseAttributes

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'view_count', 'last_update']
    list_per_page = 25
    search_fields = ['title']
    inlines = [CourseAttributesInline]
    readonly_fields = ['view_count']
    prepopulated_fields = {
        'slug': ['title']
    }

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'field']
    list_per_page = 25
    search_fields = ['name', 'field']


@admin.register(Prereg)
class PreregAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'course', 'created']
    list_per_page = 25
    search_fields = ['name', 'email', 'phone', 'course']