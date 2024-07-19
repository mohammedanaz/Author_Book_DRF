
from django.urls import path
from .views import (
    GetABookView, 
    ListCreateBookView,
    SignupView,
    UpdateDeleteBook,
    )
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('get_a_book/<int:pk>/', GetABookView.as_view(), name='get_a_books'),
    path('list_create_books/', ListCreateBookView.as_view(), name='list_create_books'),
    path('update_delete_book/<int:pk>/', UpdateDeleteBook.as_view(), name='update_delete_book'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]