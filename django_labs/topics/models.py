from django.db import models

# Create your models here.
class Topic:
    title = models.CharField(max_length=256)
