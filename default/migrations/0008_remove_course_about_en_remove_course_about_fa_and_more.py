# Generated by Django 5.0.7 on 2024-07-25 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0007_course_about_en_course_about_fa_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='about_en',
        ),
        migrations.RemoveField(
            model_name='course',
            name='about_fa',
        ),
        migrations.RemoveField(
            model_name='course',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='course',
            name='description_fa',
        ),
        migrations.RemoveField(
            model_name='course',
            name='last_update_en',
        ),
        migrations.RemoveField(
            model_name='course',
            name='last_update_fa',
        ),
        migrations.RemoveField(
            model_name='course',
            name='slug_en',
        ),
        migrations.RemoveField(
            model_name='course',
            name='slug_fa',
        ),
        migrations.RemoveField(
            model_name='course',
            name='teachers_en',
        ),
        migrations.RemoveField(
            model_name='course',
            name='teachers_fa',
        ),
        migrations.RemoveField(
            model_name='course',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='course',
            name='title_fa',
        ),
        migrations.RemoveField(
            model_name='course',
            name='video_en',
        ),
        migrations.RemoveField(
            model_name='course',
            name='video_fa',
        ),
        migrations.RemoveField(
            model_name='course',
            name='view_count_en',
        ),
        migrations.RemoveField(
            model_name='course',
            name='view_count_fa',
        ),
    ]