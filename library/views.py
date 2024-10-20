from django.shortcuts import render
from rest_framework import generics
from .models import Book, LibraryUser, Transaction
from .serializers import BookSerializer, LibraryUserSerializer, TransactionSerializer
from rest_framework.response import response
from rest_framework.views import APIView

# Book Views (CRUD)
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Library User Views (CRUD)
class LibraryUserListCreateView(generics.ListCreateAPIView):
    queryset = LibraryUser.objects.all()
    serializer_class = LibraryUserSerializer

class LibraryUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LibraryUser.objects.all()
    serializer_class = LibraryUserSerializer

# Transaction Views (Check-out and Return Books)
class TransactionListCreateView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    
    class APIRootView(APIView):
        def get(self, request):
            return Response({
            "books": "/api/books/",
            "users": "/api/users/",
            "transactions": "/api/transactions/",
            })

