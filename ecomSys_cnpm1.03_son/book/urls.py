from django.urls import path
from .views import BookView

urlpatterns = [
    path('book/', BookView.as_view(), name='book-list'),
    path('book/<int:id>/', BookView.as_view(), name='book-detail'),
]