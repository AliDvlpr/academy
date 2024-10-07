from django.urls import path
from .views import *

urlpatterns = [
    path('upload_resume/', upload_resume_view, name='upload_resume'),
    path('hiring/', hiring_form_view, name='hiring_form'),
]