# Generated by Django 5.0.7 on 2024-10-06 12:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0008_remove_course_about_en_remove_course_about_fa_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'دوره', 'verbose_name_plural': 'دوره\u200cها'},
        ),
        migrations.AlterModelOptions(
            name='courseattributes',
            options={'verbose_name': 'ویژگی دوره', 'verbose_name_plural': 'ویژگی های دوره'},
        ),
        migrations.AlterModelOptions(
            name='prereg',
            options={'verbose_name': 'پیش ثبت نام', 'verbose_name_plural': 'پیش ثبت نام کنندگان'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': 'استاد', 'verbose_name_plural': 'اساتید'},
        ),
        migrations.AlterField(
            model_name='course',
            name='about',
            field=models.TextField(blank=True, null=True, verbose_name='درباره'),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='course',
            name='last_update',
            field=models.DateTimeField(auto_now=True, verbose_name='آخرین آپدیت'),
        ),
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='تگ'),
        ),
        migrations.AlterField(
            model_name='course',
            name='teachers',
            field=models.ManyToManyField(related_name='courses', to='default.teacher', verbose_name='اساتید'),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=255, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='course',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos_uploaded', verbose_name='ویدیو'),
        ),
        migrations.AlterField(
            model_name='course',
            name='view_count',
            field=models.IntegerField(default=0, verbose_name='تعداد بازدید'),
        ),
        migrations.AlterField(
            model_name='courseattributes',
            name='attribute',
            field=models.TextField(verbose_name='ویژگی'),
        ),
        migrations.AlterField(
            model_name='courseattributes',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attributes', to='default.course', verbose_name='دوره'),
        ),
        migrations.AlterField(
            model_name='prereg',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='preregs', to='default.course', verbose_name='دوره'),
        ),
        migrations.AlterField(
            model_name='prereg',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ پیش ثبت نام'),
        ),
        migrations.AlterField(
            model_name='prereg',
            name='email',
            field=models.EmailField(blank=True, max_length=225, null=True, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='prereg',
            name='name',
            field=models.CharField(max_length=255, verbose_name='اسم'),
        ),
        migrations.AlterField(
            model_name='prereg',
            name='phone',
            field=models.CharField(max_length=11, verbose_name='شماره موبایل'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='field',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='شاخه'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images_uploaded', verbose_name='عکس'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='name',
            field=models.CharField(max_length=255, verbose_name='اسم'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
    ]
