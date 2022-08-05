from turtle import title
from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(blank=True)