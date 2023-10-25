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