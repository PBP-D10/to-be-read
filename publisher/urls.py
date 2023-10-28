from django.urls import path
from .views import get_publisher_house, houses, edit_book

app_name = 'publisher'

urlpatterns = [
    path('get-houses/', get_publisher_house, name='get_publisher_house'),
    path('houses/', houses, name='houses'),
    path('edit-book/<int:book_id>/', edit_book, name='edit_book'),
]
