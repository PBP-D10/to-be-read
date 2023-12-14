from django.urls import path
from . import views

urlpatterns = [
    # path('', get_books, name='get_books'),
    path('add/<int:book_id>', views.create_review, name='Add review'),
]
