from django.db import models

# Create your models here.
class VideoModel(models.Model):
    video_name = models.FileField(upload_to='video/', blank=True, null=True)
    