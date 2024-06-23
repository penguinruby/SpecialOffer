from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_number = models.CharField(max_length=255, blank=True, null=True)
    product_number_2 = models.CharField(max_length=255, blank=True, null=True)
    currency = models.CharField(max_length=10, blank=True, null=True)
    price = models.CharField(max_length=20, blank=True, null=True)
    brand_name = models.CharField(max_length=255, blank=True, null=True)
    product_url = models.URLField(max_length=500, blank=True, null=True)
    product_picture_url = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.product_name
