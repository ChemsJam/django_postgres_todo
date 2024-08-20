from django.db import models

# Create your models here.
class Task(models.Model):
    tittle = models.CharField(max_length=100, default=' ')
    description = models.TextField(blank=True)