from django.urls import path
from . import views

app_name = 'publisher'

urlpatterns = [
    path('create/', views.create_book, name='create_book'),
    path('delete/<int:id>/', views.delete_book, name='delete_book'),
    path('check/', views.check_is_publisher, name='check_is_publisher'),
]
