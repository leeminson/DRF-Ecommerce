import requests
from rest_framework import serializers

from shipment import models
class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Shipment
        fields='__all__'
        