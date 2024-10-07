from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from .forms import *
# Create your views here.

class FormViewSet(ModelViewSet):
    http_method_names = ['post']
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    
def upload_resume_view(request):
    if request.method == 'POST':
        form = PdfForm(request.POST, request.FILES)
        if form.is_valid():
            pdf = form.save()
            return JsonResponse({'success': True, 'resume_id': pdf.id})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

def hiring_form_view(request):
    if request.method == 'POST':
        form = HiringFormForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = HiringFormForm()
    return render(request, 'forms/hiring.html', {'form': form})

class PdfViewSet(ModelViewSet):
    http_method_names = ['post']
    queryset = Pdf.objects.all()
    serializer_class = PdfSerializer

class LogViewSet(ModelViewSet):
    http_method_names = ['post']
    queryset = Log.objects.all()
    serializer_class = LogSerializer