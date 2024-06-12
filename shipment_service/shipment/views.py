from django.shortcuts import render
from rest_framework import generics

from shipment.models import Shipment
from shipment.serializers import ShipmentSerializer
# Create your views here.
class ShipmentListCreateView(generics.ListCreateAPIView):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer

class ShipmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer