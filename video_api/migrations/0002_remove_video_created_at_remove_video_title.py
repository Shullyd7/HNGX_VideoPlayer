# Generated by Django 4.2.5 on 2023-09-29 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='video',
            name='title',
        ),
    ]
