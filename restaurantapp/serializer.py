from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    Category_Fr = CategorySerializer()
    class Meta:
        model = Product
        fields = '__all__'


class StockSerializer(serializers.ModelSerializer):
    Product = ProductSerializer()
    class Meta:
        model = Stock
        fields = '__all__'
        
class attributecategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = attributecategory
        fields = '__all__'

