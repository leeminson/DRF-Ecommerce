from django.urls import path

from order.views import OrderDetailView, OrderListCreateView
urlpatterns = [
    path('order/', OrderListCreateView.as_view(), name='order-list-create'),
    path('order/<int:id>/', OrderDetailView.as_view(), name='order-retrieve'),
]