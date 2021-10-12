from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here

class Brand(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    sku = models.CharField(max_length=200)
    name = models.CharField(max_length=300)
    price = models.FloatField()
    queries = models.IntegerField()
    id_brand = models.ForeignKey(Brand, related_name='brands', on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('auth.User', related_name='products', on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.sku} {self.name}'
