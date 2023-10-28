from django.urls import path
from . import views

app_name = 'publisher'

urlpatterns = [
    path('create/', views.create_book, name='create_book'),
    path('delete/<int:id>/', views.delete_book, name='delete_book'),
    # Add other urls as required
]
