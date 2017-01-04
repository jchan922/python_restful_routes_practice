from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.CharField(max_length=1000)
    product_price = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_At = models.DateTimeField(auto_now=True)
