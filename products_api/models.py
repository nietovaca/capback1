from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    amount = models.IntegerField(default=1)

    class Meta: 
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def __str__(self):
        return self.title 