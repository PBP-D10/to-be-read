from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm
from django.http import JsonResponse

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    else:
        form = BookForm()
    return render(request, 'create_book.html', {'form': form})

def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return redirect('Home')
