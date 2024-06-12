from rest_framework import serializers

from .models import Mobile, MobileBrand
class MobileBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model=MobileBrand
        fields=["name"]
class MobileSerializer(serializers.ModelSerializer):
    brand=MobileBrandSerializer()
    class Meta:
        model=Mobile
        fields=["name","slug","brand","image","description","price","is_available","meta_keywords","meta_description","created_at","cpu","ram","brand","display_size","storage_capacity"]