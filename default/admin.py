from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from django.utils.html import format_html
from .models import *


class CourseAttributesInline(TabularInline):
    model = CourseAttributes


@admin.register(Course)
class CourseAdmin(ModelAdmin):
    list_display = ['title', 'slug', 'view_count', 'last_update']
    list_per_page = 25
    search_fields = ['title']
    inlines = [CourseAttributesInline]
    readonly_fields = ['view_count']
    prepopulated_fields = {
        'slug': ['title']
    }


@admin.register(Teacher)
class TeacherAdmin(ModelAdmin):
    list_display = ['name', 'thumbnail', 'field']
    list_per_page = 25
    search_fields = ['name', 'field']

    def thumbnail(self, instance):
        if instance.image:
            return format_html(f'<img src="{instance.image.url}" style="width: 40px; height: 40px; border-radius: 40px;" />')
        return 'No Image'
    
    thumbnail.short_description = 'عکس'


@admin.register(Prereg)
class PreregAdmin(ModelAdmin):
    list_display = ['name', 'email', 'phone', 'course', 'created']
    list_per_page = 25
    list_filter = ['course']
