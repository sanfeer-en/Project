from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Unit)

class sadmin (admin.ModelAdmin):
    list_display = ['UnitValue', 'UnitName']
admin.site.register(Category)

admin.site.register(Tax)

admin.site.register(attributecategory)

admin.site.register(Attribute)

admin.site.register(Product)