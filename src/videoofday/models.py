from django.db import models

# Create your models here.
class Video(models.Model):
    url = models.URLField()
    publish_date = models.DateTimeField()
    name = models.TextField(default="", max_length=1000)
    description = models.TextField(default="", max_length=10000)
