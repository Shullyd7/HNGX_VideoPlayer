# Generated by Django 4.2.5 on 2023-09-30 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video_api', '0005_video_transcript'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='transcript',
        ),
    ]
