
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveAPIView

from user.models import User
from .serializers import UserRegistrationSerializer, UserSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.views import APIView
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

