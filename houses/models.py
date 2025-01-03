from django.db import models


# Create your models here.
class House(models.Model):
    """Model Definition for Houses"""

    name = models.CharField(max_length=140)
    price = models.PositiveIntegerField()
    description = models.TimeField()
    address = models.CharField(max_length=140)
