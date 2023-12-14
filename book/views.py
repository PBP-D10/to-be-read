from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from book.models import Book
from django.db.models import Q # untuk chain filter
from django.views.decorators.csrf import csrf_exempt # untuk get_books_json

# Create your views here.
def get_all_books(request):
    books = Book.objects.all().order_by('-date_added')
    books_json = serializers.serialize('json', books)
    return HttpResponse(books_json, content_type='application/json')

def home_page(request):
    books = Book.objects.all().order_by('-date_added')
    context = {'books': books}
    return render(request, 'home.html', context)

@csrf_exempt
def get_books_json(request):
    if request.method == "POST":
        keyword =  request.POST.get("keyword") or ""

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
        return HttpResponse(serializers.serialize("json", books), content_type="application/json")
    else:
        keyword = ""
        books = Book.objects.all()
        books = books.order_by('-date_added')
        return HttpResponse(serializers.serialize("json", books), content_type="application/json")

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    context = {
        'book': book,
    }
    return render(request, 'book_detail.html', context=context)

