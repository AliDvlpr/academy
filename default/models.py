from django.conf import settings
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from .validators import *

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name=_('اسم'))
    image = models.ImageField(upload_to="images_uploaded",null=True, blank=True, verbose_name=_('عکس'))
    field = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('شاخه'))
    description = models.TextField(null=True, blank=True, verbose_name=_('توضیحات'))
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('کاربر'))

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = _('استاد')
        verbose_name_plural = _('اساتید')


class Course(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name=_('عنوان'))
    slug = models.SlugField(unique=True, verbose_name=_('تگ'))
    video = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True, verbose_name=_('توضیحات'))
    about = models.TextField(null=True, blank=True, verbose_name=_('درباره'))
    last_update = models.DateTimeField(auto_now=True, verbose_name=_('آخرین آپدیت'))
    teachers = models.ManyToManyField(Teacher, related_name='courses', verbose_name=_('اساتید'))
    view_count = models.IntegerField(default=0, verbose_name=_('تعداد بازدید'))

    def __str__(self) -> str:
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = _('دوره')
        verbose_name_plural = _('دوره‌ها')

class CourseAttributes(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="attributes", verbose_name=_('دوره'))
    attribute = models.TextField(verbose_name=_('ویژگی'))
    gif = models.FileField(upload_to='gifs_uploaded', validators=[validate_big_file_size],null=True, blank=True, verbose_name=_('گیف'))

    def __str__(self):
        return f"{self.course.title} - {self.attribute}"
    
    class Meta:
        verbose_name = _('ویژگی دوره')
        verbose_name_plural = _('ویژگی های دوره')

class Prereg(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name=_('اسم'))
    phone = models.CharField(max_length=11, null=False, blank=False, verbose_name=_('شماره موبایل'))
    email = models.EmailField(max_length=225, null=True, blank=True, verbose_name=_('ایمیل'))
    course = models.ForeignKey(Course, on_delete=models.PROTECT, related_name='preregs', verbose_name=_('دوره'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('تاریخ پیش ثبت نام'))

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = _('پیش ثبت نام')
        verbose_name_plural = _('پیش ثبت نام کنندگان')

class Log(models.Model):
    ip = models.CharField(max_length=15, null=False, blank=False)
    logged = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.ip