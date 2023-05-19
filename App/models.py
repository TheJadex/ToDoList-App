from django.db import models

# Create your models here.

class List(models.Model):
    list = models.CharField(max_length=20)