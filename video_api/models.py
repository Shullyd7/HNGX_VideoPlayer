from django.db import models

# Create your models here.


class Video(models.Model):
    upload = models.FileField(upload_to='videos/')
    transcription = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.id)