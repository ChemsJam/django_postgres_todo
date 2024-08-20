from django.db import models

# Create your models here.
class Task(models.Model):
    tittle = models.CharField(max_length=50),
    description = models.TextField(blank=True)