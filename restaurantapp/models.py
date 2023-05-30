from django.db import models

# Create your models here.
class Unit(models.Model):
    UnitName=models.CharField(max_length=200)
    UnitValue=models.IntegerField()
    
    def __str__(self):
        return self.UnitName
class Category(models.Model):
    Namecategory = models.CharField(max_length=200)
    Imagecategory=models.ImageField(upload_to="images/")

    def __str__(self):
        return self.Namecategory
class Tax(models.Model):
    Taxname = models.CharField(max_length=200)
    Taxpercentage =models.IntegerField()

    def __str__(self):
        return self.Taxname
        
class attributecategory(models.Model):
    attributeName = models.CharField(max_length=100)

    def __str__(self):
        return self.attributeName
        

    