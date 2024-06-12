import requests
from rest_framework import serializers
from .models import Cart, CartItem
class CartItemSerializer(serializers.ModelSerializer):
    # Define fields for product name and price
    product_name = serializers.SerializerMethodField()
    product_price = serializers.SerializerMethodField()
    class Meta:
        model = CartItem
        fields = ['id', 'cart', 'product_id', 'date_added', 'quantity', 'product_name', 'product_price']
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
class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'user_id', 'date', 'cart_items', 'total'] 

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
class CreateCartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields = ['id', 'user_id', 'date']
class AddCartItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()
    def save(self, **kwargs):
        user_id = self.context["cart_id"]
        cart ,created= Cart.objects.get_or_create(user_id=user_id)
        product_id = self.validated_data["product_id"] 
        quantity = self.validated_data["quantity"] 
        try:
            # Check if the cart item already exists
            cartitem = CartItem.objects.get(product_id=product_id, cart=cart)
            # If it exists, update the quantity
            cartitem.quantity += quantity
            cartitem.save()
        except CartItem.DoesNotExist:
                # If it does not exist, create a new cart item
            cartitem = CartItem.objects.create(
                cart=cart,
                product_id=product_id,
                quantity=quantity
            )

        
        self.instance = cartitem
        return self.instance
    class Meta:
        model = CartItem
        fields = ["id", "product_id", "quantity"]
class UpdateCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ["quantity"]
        