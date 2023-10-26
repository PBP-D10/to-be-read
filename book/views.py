from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from book.models import Book

# Create your views here.
def home_page(request):
    books = Book.objects.all().order_by('-date_added')
    context = {
        'books': books,
    }
    return render(request, 'home.html', context=context)

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    context = {
        'book': book,
    }
    return render(request, 'book_detail.html', context=context)

