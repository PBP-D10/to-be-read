from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound, HttpResponse
from book.models import SavedBook, Book
from django.views.decorators.csrf import csrf_exempt
from reader.models import Profile
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from reader.forms import SavedForm
from django.http import JsonResponse
from django.core import serializers
# Create your views here.
@login_required(login_url='login')
@csrf_exempt
def show_saved(request):       
    # saved_books = SavedBook.objects.filter(owner=request.user)
    # context = {
    #     'name': request.user.username,
    #     'saved_books': saved_books,
    # }
    # if request.method =='POST':
    #     selected_value = request.POST.get('selected_value')
    #     if selected_value == "year":
    #         saved_books = saved_books.order_by("-year")

    # return render(request, "my_tbr.html", context)
    # views.py
    saved_books = SavedBook.objects.filter(owner=request.user)
    form = SavedForm(request.POST or None)

    if request.method == 'POST' : #and request.is_ajax():

        if form.is_valid():
            selected_value = form.cleaned_data['selected_value']
            if selected_value != 'date_added':
                saved_books = saved_books.order_by(selected_value)

    context = {
        'saved_books': saved_books,
        'form': form,
    }
    return render(request, "my_tbr.html", context)
    #return HttpResponse(status=400)  # Bad request if the form is not valid or the request is not Ajax

@csrf_exempt
def create_ajax(request):
    if request.method == 'POST':
        book_id = request.POST.get("book")

        new_book = SavedBook.objects.get_or_create(owner=request.user, book_id=book_id)
        if (new_book[1] == False):
            return HttpResponse(b"ALREADY_EXISTS", status=200)
        else:
            new_book[0].save()
        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def view_profile(request):
    current_profile = Profile.objects.get(user=request.user)
    context = {'profile':current_profile}
    return render(request, "view_profile.html", context)

def edit_profile(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        date_of_birth = request.POST.get('date_of_birth')
        
        if name != profile.name:
            profile.name = name
        if email != profile.email:
            profile.email = email
        if address != profile.address:
            profile.address = address
        if date_of_birth != profile.date_of_birth:
            profile.date_of_birth = date_of_birth
        
        profile.save()
        return HttpResponseRedirect(reverse('reader:view_profile'))

    context = {'profile': profile}
    return render(request, "edit_profile.html", context)

def saved_detail(request, book_id):
    book = Book.objects.get(id =book_id)
    context = {
        'book': book,
    }
    return render(request, 'saved_detail.html', context=context)
