import requests
from rest_framework import serializers

from payment import models
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Payment
        fields='__all__'