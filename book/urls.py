from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    # path('', get_books, name='get_books'),
    path('', views.home_page, name='Home'),
    path('books/<int:book_id>/', views.book_detail, name='Book Detail'),
]