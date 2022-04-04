from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.CharField(max_length=255, default="New")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='')
    primary_image = models.ImageField(blank=True, upload_to='img/', null=True)
    secondary_image = models.ImageField(blank=True, upload_to='img/', null=True)
    imgURL = models.TextField (null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=1.99)
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