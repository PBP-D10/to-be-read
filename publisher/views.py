from django.shortcuts import *
from django.http import *
from .models import PublisherHouse
from book.models import Book
from .forms import BookForm
from .decorators import publisher_required

def get_publisher_house(request):
    publisher_houses = PublisherHouse.objects.all()
    data = [{'name': house.publisher.name, 'year_established': house.year_established} for house in publisher_houses]
    return JsonResponse(data, safe=False)

def houses(request):
    return render(request, 'publisher_house_page.html')

@publisher_required
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book:Home')
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    else:
        form = BookForm(instance=book)
    
    return render(request, 'edit_book.html', {'form': form, 'book': book})
