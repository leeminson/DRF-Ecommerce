from django.urls import path
from .views import ClothesView

urlpatterns = [
    path('clothes/', ClothesView.as_view(), name='clothes-list'),
    path('clothes/<int:id>/', ClothesView.as_view(), name='clothes-detail'),
]