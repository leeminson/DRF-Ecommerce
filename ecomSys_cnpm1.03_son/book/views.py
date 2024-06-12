from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from book.models import Book
from rest_framework import status
from book.serializer import BookSerializer

# Create your views here.
class BookView(APIView):
	def get(self, request, id=None):
		if id is not None:
				result = Book.objects.get(id=id)  
				serializer = BookSerializer(result)  
				return Response({'success': 'success', "students":serializer.data}, status=200)
		else:		
				books=Book.objects.all()
				serializer=BookSerializer(books,many=True)
				return Response({'success': 'success', "books":serializer.data}, status=200)
	def post(self,request):
			serializer = BookSerializer(data=request.data)  
			if serializer.is_valid():  
				serializer.save()  
				return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
			else:  
				return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
	def patch(self, request, id):  
			result = Book.objects.get(id=id)  
			serializer = BookSerializer(result, data = request.data, partial=True)  
			if serializer.is_valid():  
				serializer.save()  
				return Response({"status": "success", "data": serializer.data})  
			else:  
				return Response({"status": "error", "data": serializer.errors})
	def delete(self, request, id=None):  
			result = get_object_or_404(Book, id=id)  
			result.delete()  
			return Response({"status": "success", "data": "Book Deleted"})  