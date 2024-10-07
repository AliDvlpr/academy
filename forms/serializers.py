from rest_framework import serializers
from .models import *

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = ['name', 'phone']

class PdfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pdf
        fields = ['id', 'pdf']

class HiringFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = HiringForm
        fields = ['name', 'phone', 'email', 'job', 'resume', 'salary']

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ['ip']