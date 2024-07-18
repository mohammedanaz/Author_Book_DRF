
from django.urls import path
from .views import GetAllBookView, ListCreateBookView

urlpatterns = [
    path('get_all_books/', GetAllBookView.as_view(), name='all_books'),
    path('create_book/', ListCreateBookView.as_view(), name='create_book'),
]