from rest_framework import serializers
from user.models import Address, FullName
from django.contrib.auth import get_user_model
User = get_user_model()
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
class FullNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = FullName
        fields = ['first_name', 'last_name']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['house_num', 'street', 'district', 'city']

class UserSerializer(serializers.ModelSerializer):
    full_name = FullNameSerializer()
    addresses = AddressSerializer(many=True)
    class Meta:
        model = User
        fields = ['emails', 'mobile', 'password', 'full_name', 'addresses']

class UserRegistrationSerializer(serializers.ModelSerializer):
    full_name = FullNameSerializer()
    addresses = AddressSerializer(many=True)

    class Meta:
        model = User
        fields = ['emails', 'mobile', 'password', 'confirm_password', 'full_name', 'addresses']

    def create(self, validated_data):
        full_name_data = validated_data.pop('full_name')
        addresses_data = validated_data.pop('addresses')
        full_name = FullName.objects.create(**full_name_data)
        user = User.objects.create(
            emails=validated_data['emails'],
            mobile=validated_data['mobile'],
            full_name=full_name
        )

        for address_data in addresses_data:
            Address.objects.create(user=user, **address_data)

        user.set_password(validated_data['password'])
        user.save()
        return user