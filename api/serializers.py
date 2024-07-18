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

    author_id = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), source='author', write_only=True)
    author_name = serializers.CharField(source='author.first_name', read_only=True)
    class Meta:
        model = Book
        fields = ['id', 'title', 'author_id', 'author_name', 'price']