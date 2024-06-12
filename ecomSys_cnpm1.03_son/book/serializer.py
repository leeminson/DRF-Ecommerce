from rest_framework import serializers

from book.models import *
class BookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=BookCategory
        fields=["name"]
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields='__all__'
class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Publisher
        fields='__all__'
class BookSerializer(serializers.ModelSerializer):
    Book_Category=BookCategorySerializer(many=True)
    authors=AuthorSerializer(many=True)
    publisher=PublisherSerializer()
    class Meta:
        model=Book
        fields=["name","slug","image","description","price","is_available","meta_keywords","meta_description","created_at","numberofpage","Book_Category","authors","publisher"]
        