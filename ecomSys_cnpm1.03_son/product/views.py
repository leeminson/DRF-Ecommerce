from urllib import request
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters
from product.models import Product
from product.serializer import ProductSerializer,ProductPolymorphicSerializer

class ProductView(generics.ListCreateAPIView):
	# def get(self, request, id=None):
	# 	if id is not None:
	# 			result = Product.objects.get(id=id)  
	# 			serializer = ProductSerializer(result)  
	# 			return Response({'success': 'success', "product":serializer.data}, status=200)
	# 	else:		
	# 			result=Product.objects.all()
	# 			serializer=ProductSerializer(result,many=True)
	# 			return Response({'success': 'success', "product":serializer.data}, status=200)
    search_fields = ['name','description','^meta_keywords','^meta_description']
    filter_backends = (filters.SearchFilter,)
    queryset=Product.objects.all()
    serializer_class=ProductPolymorphicSerializer
class ProductDetailView(generics.ListAPIView):
    serializer_class = ProductPolymorphicSerializer
    def get_queryset(self):
        product_id = self.kwargs['id']
        return Product.objects.filter(id=product_id)