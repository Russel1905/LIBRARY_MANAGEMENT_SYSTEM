from django.urls import path

from .views import (
    BookListCreateView, BookDetailView,
    LibraryUserListCreateView, LibraryUserDetailView,
    TransactionListCreateView,APIRootView,LibraryUserListCreateView, LibraryUserDetailView,
)

urlpatterns = [
    path('', APIRootView.as_view(), name='api-root'),
    path('books/', BookListCreateView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('users/', LibraryUserListCreateView.as_view(), name='user-list'),
    path('users/<int:pk>/', LibraryUserDetailView.as_view(), name='user-detail'),
    path('transactions/', TransactionListCreateView.as_view(), name='transaction-list'),
]
