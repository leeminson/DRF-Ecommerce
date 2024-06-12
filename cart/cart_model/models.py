from django.db import models
import requests

# Create your models here.
class Cart(models.Model):
    user_id=models.IntegerField(unique=True)
    date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=25)
    def add_item(self, product_id, quantity=1):
        existing_item = self.cart_items.filter(product_id=product_id).first()
        if existing_item:
            existing_item.quantity += quantity
            existing_item.save()
        else:
            CartItem.objects.create(cart=self, product_id=product_id, quantity=quantity)
class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,related_name="cart_items")
    product_id=models.IntegerField()
    date_added=models.DateField(auto_now_add=True)
    quantity=models.IntegerField()

