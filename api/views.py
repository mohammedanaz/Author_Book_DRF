from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from .models import Book, Author
from django.contrib.auth.models import User
from .serializers import BookSerializer, AuthorSerializer, UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination


def get_tokens_for_user(user):
    '''
    This function returns an object with access token and refresh token.
    '''
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class SignupView(generics.CreateAPIView):
    '''
    to create new user instance in User model after validation.
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GetABookView(APIView):
    '''
    to retrieve a particular book with id.
    '''
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, *args, **kwargss):
        try:
            book = Book.objects.get(pk=pk)
        except Exception as e:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(instance=book)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BookPagination(PageNumberPagination):
    '''
    to paginate response.
    '''
    page_size = 3
    
    
class ListCreateBookView(generics.ListCreateAPIView):
    '''
    to create a book instance or list all books.
    '''
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = BookPagination


class UpdateDeleteBook(generics.RetrieveUpdateDestroyAPIView):
    '''
    to update ot delete a book instance.
    '''
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        try:
            response = super().destroy(request, *args, **kwargs)
            return Response({"detail": "Book has been deleted."}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": f"{str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

    