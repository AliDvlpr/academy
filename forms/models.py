from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Form(models.Model):
    name = models.CharField(max_length=255,null=False,blank=False)
    phone = models.CharField(max_length=11, unique=True, null=False, blank=False)

# 👆 Simple registration form

class HiringForm(models.Model):
    name = models.CharField(max_length=255,null=False,blank=False)
    phone = models.CharField(max_length=11, unique=True, null=False, blank=False)
    email = models.EmailField(max_length=225, null=True, blank=True)
    job = models.CharField(max_length=255, null=True, blank=True)
    resume = models.OneToOneField('pdf', on_delete=models.CASCADE, null=False, blank=False)
    salary = models.DecimalField(
        max_digits=20,
        decimal_places=0,
        validators=[MinValueValidator(1)])

# 👆 Hiring registration form

class Pdf(models.Model):
    pdf = models.FileField(upload_to="files")

# 👆 Uploading resume pdf file

class Log(models.Model):
    ip = models.CharField(max_length=15, null=False, blank=False)
    FORM_SIMPLE = 'S'
    FORM_HIRING = 'H'

    FORM_CHOICES = [
        (FORM_SIMPLE, 'Simple Forms'),
        (FORM_HIRING, 'Hiring Forms'),
    ]
    form = models.CharField(
        max_length=1, choices=FORM_CHOICES, default=FORM_SIMPLE)
    logged = models.DateTimeField(auto_now_add=True)

# 👆 Simple IPv4 logger