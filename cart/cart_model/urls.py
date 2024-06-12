from django.urls import path
from .views import CartItemViewSet, CartListCreateView, CartDetailView

urlpatterns = [
    path('carts/', CartListCreateView.as_view(), name='cart-list-create'),
    path('carts/<int:id>/', CartDetailView.as_view(), name='cart-retrieve'),
    path('carts/<int:cart_pk>/items/', CartItemViewSet.as_view({'get': 'list', 'post': 'create'}), name='cart-item-list'),
    path('carts/<int:cart_pk>/items/<int:pk>/', CartItemViewSet.as_view({'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy'}), name='cart-item-detail'),
]
    # Define other URL patterns for additional views if needed