from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseNotFound
from book.models import SavedBook

# Create your views here.
@login_required(login_url='login')
def show_saved(request):
    saved_books = SavedBook.objects.filter(owner=request.user)
    context = {
        'name': request.user.username,
        'saved_books': saved_books,
    }

    return render(request, "my_tbr.html", context)

def remove_book(request, id):
    saved_book = SavedBook.objects.get(pk=id)
    saved_book.delete()
    return redirect('reader:show_saved')