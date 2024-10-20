from django.db import models

# Create your models here.
class ContactUs(models.Model):
    phone = models.CharField(max_length=15)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.phone