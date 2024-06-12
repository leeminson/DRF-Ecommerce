
from django.db import models
# Create your models here.


from product.models import *

class MobileBrand(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Mobile(Product):
    cpu = models.CharField(max_length=100)
    ram = models.IntegerField()
    brand = models.ForeignKey(MobileBrand,on_delete=models.CASCADE)
    release_date = models.DateField()
    display_size = models.FloatField()
    storage_capacity = models.PositiveIntegerField()