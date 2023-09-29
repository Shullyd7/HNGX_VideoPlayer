from django.db import models

# Create your models here.

class Video(models.Model):
    upload = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.title
