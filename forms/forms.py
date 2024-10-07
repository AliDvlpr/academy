from django import forms
from django.core.exceptions import ValidationError
from .models import Pdf, HiringForm

class PdfForm(forms.ModelForm):
    class Meta:
        model = Pdf
        fields = ['pdf']
        labels = {
            'pdf': 'رزومه',
        }
        widgets = {
            'pdf': forms.FileInput(attrs={'class': 'form-control'}),
        }

def validate_phone(value):
    if not value.startswith('09') or not value.isdigit() or len(value) != 11:
        raise ValidationError('شماره تلفن باید با 09 شروع شود و 11 رقم باشد.')

class HiringFormForm(forms.ModelForm):
    phone = forms.CharField(
        max_length=11,
        validators=[validate_phone],
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'شماره تلفن شما'})
    )

    class Meta:
        model = HiringForm
        fields = ['name', 'phone', 'email', 'job', 'resume', 'salary']
        labels = {
            'name': 'نام کامل',
            'phone': 'شماره تلفن',
            'email': 'ایمیل',
            'job': 'شغل',
            'resume': 'رزومه',
            'salary': 'مبلغ پیشنهادی',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کامل شما'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل شما'}),
            'job': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'شغل شما'}),
            'resume': forms.HiddenInput(),  # Hidden input to store the resume ID
            'salary': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'مبلغ پیشنهادی شما'}),
        }