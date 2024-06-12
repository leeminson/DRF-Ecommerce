from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from clothes.serializer import ClothesSerializer
from .models import *
# Create your views here.
class ClothesView(APIView):  

    def get(self, request, id=None):  
        if id is not None:
            result = Clothes.objects.get(id=id)  
            serializers = ClothesSerializer(result)  
            return Response({'success': 'success', "clothes":serializers.data}, status=200)  
        else:
            result = Clothes.objects.all()  
            serializers = ClothesSerializer(result, many=True)  
            return Response({'status': 'success', "clothes":serializers.data}, status=200)  