from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics
from .models import Cart, CartItem
from .serializers import AddCartItemSerializer, CartSerializer, CartItemSerializer, CreateCartSerializer, UpdateCartItemSerializer
import requests
from rest_framework.viewsets import ModelViewSet, GenericViewSet
class CartListCreateView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    def get_serializer_class(self):
        if self.request.method == "POST":
            return CreateCartSerializer
        return CartSerializer
class CartDetailView(generics.ListAPIView):
    serializer_class = CartSerializer
    def get_queryset(self):
        user_id = self.kwargs['id']
        return Cart.objects.filter(user_id=user_id)
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        # Retrieve cart items associated with the cart
        cart_items = CartItem.objects.filter(cart=instance)
        cart_item_serializer = CartItemSerializer(cart_items, many=True)
        # Add cart items data to the response
        response_data = serializer.data
        response_data['cart_items'] = cart_item_serializer.data
        return Response(response_data)
class CartItemViewSet(ModelViewSet):
    http_method_names = ["get", "post", "patch", "delete"]
    def get_queryset(self):
        user_id=self.kwargs["cart_pk"]
        cart=Cart.objects.filter(user_id=user_id).first()
        return CartItem.objects.filter(cart=cart)
    def get_serializer_class(self):
        if self.request.method == "POST":
            return AddCartItemSerializer
        
        elif self.request.method == 'PATCH':
            return UpdateCartItemSerializer
        
        return CartItemSerializer
    
    def get_serializer_context(self):
        return {"cart_id": self.kwargs["cart_pk"]}