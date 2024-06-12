import requests
from rest_framework import serializers

from order.models import Order,OrderItem

class OrderItemsSerializer(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField()
    product_price = serializers.SerializerMethodField()
    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product_id', 'quantity', 'product_name', 'product_price']
    def get_product_name(self, obj):
        # Access the product_id from the CartItem object and fetch its name
        product_id = obj.product_id
        product_info = self.get_product_info(product_id)
        return product_info.get('name', '')

    def get_product_price(self, obj):
        # Access the product_id from the CartItem object and fetch its price
        product_id = obj.product_id
        product_info = self.get_product_info(product_id)
        return product_info.get('price', 0)

    def get_product_info(self, product_id):
        # Fetch product data from the API using the product_id
        # You can implement the logic here to fetch product info from your API
        # Return a dictionary containing the name and price of the product
        # For example:
        product_api_url = f'http://127.0.0.1:8081/api/product/{product_id}'
        response = requests.get(product_api_url)
        if response.status_code == 200:
            product_data = response.json()
            return {
                'name': product_data[0].get('name', ''),
                'price': product_data[0].get('price', 0)
            }
        return {'name': '', 'price': 0}
class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemsSerializer(many=True)
    class Meta:
        model = Order
        fields = ['id', 'user_id', 'placed_at','order_items','total','pending_status'] 
    def get_total(self, obj):
        cart_items = obj.cart_items.all() 
        total = sum(self.get_item_price(item) * item.quantity for item in cart_items) 
        return total

    def get_item_price(self, item):
        # Fetch the price of the item's product from the API
        product_id = item.product_id
        product_info = self.get_product_info(product_id)
        return product_info.get('price', 0)

    def get_product_info(self, product_id):
        # Fetch product data from the API using the product_id
        product_api_url = f'http://127.0.0.1:8081/api/product/{product_id}'
        response = requests.get(product_api_url)
        if response.status_code == 200:
            product_data = response.json()
            return {
                'price': product_data[0].get('price', 0)
            }
        return {'price': 0}
class CreateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user_id', 'placed_at','pending_status']
class UpdateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['pending_status']