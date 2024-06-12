from django.shortcuts import render
from rest_framework import generics

from payment.models import Payment
from payment.serializers import PaymentSerializer
# Create your views here.
class PaymentListCreateView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
class PaymentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer