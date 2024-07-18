
from django.urls import path
from .views import GetAllBookView

urlpatterns = [
    path('get_all_books/', GetAllBookView.as_view(), name='all_books'),
]