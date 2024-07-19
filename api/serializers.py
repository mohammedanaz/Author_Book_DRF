from rest_framework import serializers
from .models import Author, Book
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    '''
    to serialize user instance.
    '''
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user


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