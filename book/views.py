from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from book.models import Book
from django.db.models import Q # untuk chain filter

# Create your views here.
def home_page(request):
    keyword =  request.GET.get("search") or ""
    if keyword == "":
        books = Book.objects.all()

    else:
        books = Book.objects.filter(Q(title__contains=keyword)
                                          | Q(author__contains=keyword)
                                          | Q(ISBN__contains=keyword))
        
    books = books.order_by('-date_added')

    context = {
        'books': books,
        'keyword': keyword
    }
    return render(request, 'home.html', context=context)