from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm

def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('publisher:book_list')
    else:
        form = BookForm()
    return render(request, 'publisher/create_book.html', {'form': form})

def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('publisher:book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'publisher/create_book.html', {'form': form})

def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return redirect('publisher:book_list')
