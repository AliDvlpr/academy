from django.conf import settings
from django.db import models
from django.utils.text import slugify

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    image = models.ImageField(upload_to="images_uploaded",null=True, blank=True)
    field = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField(unique=True)
    video = models.FileField(upload_to='videos_uploaded',null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    last_update = models.DateTimeField(auto_now=True)
    teachers = models.ManyToManyField(Teacher, related_name='courses')

    def __str__(self) -> str:
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class CourseAttributes(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="attributes")
    attribute = models.TextField()

    def __str__(self):
        return f"{self.course.title} - {self.attribute}"

class Prereg(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    phone = models.CharField(max_length=11, unique=True, null=False, blank=False)
    email = models.EmailField(max_length=225, null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.PROTECT, related_name='preregs')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class Log(models.Model):
    ip = models.CharField(max_length=15, null=False, blank=False)
    logged = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.ip