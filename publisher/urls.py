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
]
