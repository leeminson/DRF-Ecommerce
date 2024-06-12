from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import *
import requests

class SearchView(APIView):
    def get(self, request):
        query = request.query_params.get('query')
        if query:
            product = requests.get('http://127.0.0.1:8081/api/product/?search={}'.format(query)).json()
        else:
            product = requests.get('http://127.0.0.1:80/api/product/').json()
        
        # Check if the request was successful
        return Response(product)  
