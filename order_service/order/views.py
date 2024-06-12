from django.shortcuts import render
from requests import Response
from rest_framework import generics

from order.models import Order, OrderItem
from order.serializers import CreateOrderSerializer, OrderItemsSerializer, OrderSerializer, UpdateOrderSerializer

# Create your views here.

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    def get_serializer_class(self):
        if self.request.method == "POST":
            return CreateOrderSerializer
        return OrderSerializer
class OrderDetailView(generics.ListAPIView):
    serializer_class = OrderSerializer
    def get_queryset(self):
        id = self.kwargs['id']
        return Order.objects.filter(id=id)
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        # Retrieve cart items associated with the cart
        order_items = OrderItem.objects.filter(order=instance)
        cart_item_serializer = OrderItemsSerializer(order_items, many=True)
        # Add cart items data to the response
        response_data = serializer.data
        response_data['order_items'] = cart_item_serializer.data
        return Response(response_data)
    