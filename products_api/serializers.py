from rest_framework import serializers 
from .models import Product

class ProductSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Product # tell django which model to use
        fields = ('id', 'category', 'title', 'description', 'image', 'price', 'in_stock', 'is_active', 'created', 'updated', 'amount',) # tell django which fields to include