from rest_framework import serializers
from .models import Author, Book

class AuthorSerializer(serializers.ModelSerializer):
    '''
    serialize the author data.
    '''

    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    """
    Serialize the book data.
    """

    class Meta:
        model = Book
        fields = '__all__'