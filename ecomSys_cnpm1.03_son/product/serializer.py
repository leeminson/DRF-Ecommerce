
from rest_framework import serializers
from book.serializer import BookSerializer
from clothes import models
from clothes.serializer import ClothesSerializer
from mobile.serializer import MobileSerializer
from product.models import Product
from book import models as bookmodel
from mobile import models as mobilemodel
from polymorphic_serializer.polymorphic_serializer import PolymorphicSerializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=["name","slug","image","description","quantity","price","is_available","meta_keywords","meta_description","created_at"]   
class ProductPolymorphicSerializer(PolymorphicSerializer):
    model_serializer_mapping={
        Product:ProductSerializer,
        models.Clothes:ClothesSerializer,
        bookmodel.Book:BookSerializer,
        mobilemodel.Mobile:MobileSerializer
    }