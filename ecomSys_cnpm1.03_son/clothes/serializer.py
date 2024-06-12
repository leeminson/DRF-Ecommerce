from rest_framework import serializers

from .models import *
class ClothesBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model=ClothesBrand
        fields='__all__'
class ClothesTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=ClothesType
        fields='__all__'
class ClothesSerializer(serializers.ModelSerializer):
    brand=ClothesBrandSerializer()
    clothes_type=ClothesTypeSerializer()
    class Meta:
        model=Clothes
        fields=["name","slug","image","description","price","is_available","meta_keywords","meta_description","created_at","brand","clothes_type","material"]