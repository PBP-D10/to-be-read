import json
from .models import PublisherHouse
from book.models import Book
from .forms import BookForm
from .decorators import publisher_required
from django.shortcuts import render, redirect
from book.models import Book
from .forms import BookForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Publisher
from django.shortcuts import get_object_or_404

def get_publisher_house(request):
    publisher_houses = PublisherHouse.objects.all()
    data = [{'name': house.name, 'year_established': house.year_established} for house in publisher_houses]
    return JsonResponse(data, safe=False)

def houses(request):
    return render(request, 'publisher_house_page.html')

@publisher_required
def edit_book(request, book_id):
    
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        data = json.loads
        if form.is_valid():
            form.save()
            return redirect('book:Home')
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    else:
        form = BookForm(instance=book)
    
    return render(request, 'edit_book.html', {'form': form, 'book': book})

@login_required(login_url='login')
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    else:
        form = BookForm()
    return render(request, 'create_book.html', {'form': form})

@csrf_exempt
def delete_book(request, id):
    try:
        book_hapus = Book.objects.get(pk=id)  # mengganti DeleteBook dengan Book
        book_hapus.delete()
        return JsonResponse({"success": "Book deleted successfully"}, status=200)

    except Exception as e:
        print("Exception type:", type(e))
        print("Exception message:", str(e))
        return JsonResponse({"error": str(e)}, status=500)

def check_is_publisher(request):
    if not request.user.is_authenticated:
        return JsonResponse({'is_publisher': False})
        
    publisher = Publisher.objects.filter(user=request.user)
    return JsonResponse({'is_publisher': publisher.exists()})

@csrf_exempt
def create_book_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_book = Book.objects.create(
            # user = request.user,
            ISBN = data["ISBN"],
            title = data["title"],
            author = data["author"],
            year = int(data["year"]),
            publisher = data["publisher"],
            image_s = data["image_s"],
            image_m = data["image_m"],
            image_l = data["image_l"],
        )

        new_book.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@csrf_exempt
def edit_book_flutter(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if request.method == "POST":
        data = json.loads(request.body)

        # Update the book object with the new data
        isbn = data['ISBN']
        title = data['title']
        author = data['author']
        year = data['year']
        publisher= data['publisher']
        image_s = data['image_s']
        image_m = data['image_m']
        image_l = data['image_l']

        book.ISBN = isbn
        book.title = title
        book.author = author
        book.year = year
        book.publisher = publisher
        book.image_s = image_s
        book.image_m = image_m
        book.image_l = image_l


        # Save the updated book object
        book.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)