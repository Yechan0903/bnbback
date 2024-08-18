from django.contrib import admin
from django.db import models

# Register your models here.
class House(models.Model):

    """Model Definition for Houses"""

    name = models.CharField(max_length=140)
    price = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=140)