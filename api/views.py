from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer

class GetAllBookView(APIView):
    '''
    to retrieve the all books.
    '''

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(instance=books)
        return Response(serializer.data, status=status.HTTP_200_OK)