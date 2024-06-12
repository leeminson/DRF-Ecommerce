from django.urls import path
from .views import ProductView,ProductDetailView

urlpatterns = [
    path('product/', ProductView.as_view(), name='product-list'),
    path('product/<int:id>/', ProductDetailView.as_view(), name='product-detail'),
]