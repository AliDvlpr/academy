# Generated by Django 5.0.6 on 2024-06-02 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0004_alter_course_video_alter_teacher_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]
