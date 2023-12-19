from django.urls import path
from . import views

app_name = 'publisher'

urlpatterns = [
    path('get-houses/', views.get_publisher_house, name='get_publisher_house'),
    path('houses/', views.houses, name='houses'),
    path('edit-book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('create/', views.create_book, name='create_book'),
    path('delete/<int:id>/', views.delete_book, name='delete_book'),
    path('check/', views.check_is_publisher, name='check_is_publisher'),
    
    path('create-book-flutter/', views.create_book_flutter, name='create_book_flutter'),
    path('edit-book-flutter/<int:book_id>', views.edit_book_flutter, name= 'edit_book_flutter'),
]
