from django.contrib import admin
from django.utils.html import format_html
from .models import *

# Register your models here.
@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone']
    list_per_page = 25
    search_fields = ['name', 'phone']

@admin.register(HiringForm)
class HiringFormAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'job', 'download_resume', 'salary']
    list_per_page = 25
    search_fields = ['name', 'phone', 'email', 'job', 'salary']

    def download_resume(self, obj):
        if obj.resume:
            return format_html('<a href="{0}" download>Download</a>', obj.resume.pdf.url)
        return "N/A"

    download_resume.short_description = "Download Resume"

@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ['ip', 'form','logged']
    list_filter = ['form']
    list_per_page = 50
    search_fields = ['ip', 'logged']