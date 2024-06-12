from django.db import models

# Create your models here.
class Order(models.Model):
    user_id=models.IntegerField()
    payment_id=models.IntegerField(null=True)
    shipment_id=models.IntegerField(null=True)
    total=models.DecimalField(max_digits=10, decimal_places=2,default=0)
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Completed'),
        (PAYMENT_STATUS_FAILED, 'Canceled'),
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    pending_status = models.CharField(
        max_length=50, choices=PAYMENT_STATUS_CHOICES, default='PAYMENT_STATUS_PENDING')
    def __str__(self):
        return self.pending_status
class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='order_items')
    product_id=models.IntegerField()
    quantity=models.IntegerField()
    def __str__(self) -> str:
        return self.product_id
