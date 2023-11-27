from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    # path('', get_books, name='get_books'),
    path('', views.home_page, name='Home'),
    path('books/<int:book_id>/', views.book_detail, name='Book Detail'),
    path('api/books/', views.get_all_books, name='Get All Books'),
    path('json/', views.get_books_json, name="get_books_json"),
    path('like-count/<int:book_id>/', views.get_like_count, name="get_like_count"),
]