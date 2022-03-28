from rest_framework import serializers 
from .models import Product
from .models import Category

class CategorySerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Category # tell django which model to use
        fields = ('name',) # tell django which fields to include


class ProductSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Product # tell django which model to use
        fields = ('category', 'created_by', 'title', 'author', 'description', 'image', 'price', 'in_stock', 'is_active', 'created', 'updated',) # tell django which fields to include