from django.db import models

# Create your models here.
class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)
    description=models.CharField(max_length=255)