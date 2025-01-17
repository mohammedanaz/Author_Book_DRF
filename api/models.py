from django.db import models

class Author(models.Model):
    '''
    store data of Author.
    '''

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{ self.first_name} - {self.last_name}'
    

class Book(models.Model):
    '''
    store data of Books. Each book has an 'author' field as FK.
    '''

    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete= models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return  f'{self.title} - {self.author}'
