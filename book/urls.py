from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    # path('', get_books, name='get_books'),
    path('', views.home_page, name='Home'),
    path('json/', views.get_books_json, name="get_books_json"),
]