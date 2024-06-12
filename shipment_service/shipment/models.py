from django.db import models

# Create your models here.
class Shipment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=100)
    payment_id=models.IntegerField()