from django.urls import path
from .views import MobileView

urlpatterns = [
    path('mobile/', MobileView.as_view(), name='book-list'),
    path('mobile/<int:id>/', MobileView.as_view(), name='book-detail'),
]