from django.db import models

from product.models import Product


# Create your models here.
class ClothesType(models.Model):
    name=models.CharField(max_length=150)
    def __str__(self):
        return self.name
class ClothesBrand(models.Model):
    name=models.CharField(max_length=255) 
    def __str__(self):
        return self.name
class Clothes(Product):
    brand=models.ForeignKey(ClothesBrand,on_delete=models.CASCADE)
    clothes_type = models.ForeignKey(ClothesType, on_delete=models.CASCADE)
    material=models.CharField(max_length=100)
    def __str__(self):
        return self.name
