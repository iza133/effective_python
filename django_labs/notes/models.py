from django.db import models
from topics.models import Topic

class Note(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField()
    topic = models.ForeignKey()