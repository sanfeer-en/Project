from django.db import models
import random

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
class Attribute(models.Model):
    attribute_category =models.ForeignKey(attributecategory,on_delete=models.CASCADE,null=True,blank=True)
    attribute_name = models.CharField(max_length=100,null=True,blank=True)
    SIZE =  'size'
    ADD_ON = 'addon'
    EXTRA = 'extra'
    VARIANT_CHOICES = [
        (SIZE, 'size'),
        (ADD_ON , 'add-on'),
        (EXTRA,  'extra'),
    ]
    Varients = models.CharField(max_length=100,choices=VARIANT_CHOICES)
    Price = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self. attribute_name
    
class Product(models.Model):
    Product_Name = models.CharField(max_length=100, null=True, blank=True)
    Category_Fr =models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    Unit_Fr = models.ForeignKey(Unit,on_delete=models.CASCADE,null=True,blank=True)
    Variant_fr = models.ManyToManyField(attributecategory,blank=True)
    Tax_Fr = models.ForeignKey(Tax,on_delete=models.CASCADE,null=True,blank=True)
    Is_for_sale = models.BooleanField(default=False,blank=True)
    Product_Image = models.ImageField(upload_to='product_images/',null=True,blank=True)
    Product_code = models.CharField(max_length=5,unique=True,null=True, blank=True,)
     
    def save(self, *args, **kwargs):
        # generate a unique 5-digit code
        while True:
            code = random.randint(10000, 99999)
            if not Product.objects.filter(Product_code=code).exists():
                self.Product_code = code
                break
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.Product_Name
class CompanyInformation(models.Model):
    Company_Name = models.CharField(max_length=100, null=True, blank=True)
    Company_Address = models.TextField(max_length=100, null=True, blank=True)
    GST_Number = models.CharField(max_length=100, null=True, blank=True)
    Country_Code = models.IntegerField(default=8,null=True, blank=True)
    Manufacturing_code = models.CharField(max_length=100, null=True, blank=True)

    def str(self):
        return self.Company_Name
class Stock(models.Model):
    Vendor_Bill_No =models.CharField(max_length=100,null=True,blank=True)
    Product=models.ForeignKey(Product,on_delete=models.CASCADE,blank=True)
    Units=models.ForeignKey(Unit,on_delete=models.CASCADE,blank=True)
    Quantity = models.PositiveIntegerField(null=True,blank=True,default=0)
    Purchasing_Amount = models.DecimalField(max_digits=10,null=True,blank=True,decimal_places=2)
    Selling_Amount = models.DecimalField(max_digits=10,null=True,blank=True,decimal_places=2)
    Manufacture_Date =models.DateField(null=True,blank=True)
    Expire_Date =models.DateField(null=True,blank=True)




    