from django.db import models

# Create your models here.
class Unit(models.Model):
    UnitName=models.CharField(max_length=200)
    UnitValue=models.IntegerField()