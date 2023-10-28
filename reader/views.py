from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound, HttpResponse
from book.models import SavedBook
from django.views.decorators.csrf import csrf_exempt
from reader.models import Profile
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core import serializers

# Create your views here.
@login_required(login_url='login')
def show_saved(request):       
    saved_books = SavedBook.objects.filter(owner=request.user)
    context = {
        'name': request.user.username,
        'saved_books': saved_books,
    }
    if request.method =='POST':
        selected_value = request.POST.get('selected_value')
        if selected_value == "year":
            saved_books = saved_books.order_by("-year")

    return render(request, "my_tbr.html", context)

def remove_book(request, id):
    saved_book = SavedBook.objects.get(pk=id)
    saved_book.delete()
    return redirect('reader:show_saved')

@csrf_exempt
def create_ajax(request):
    if request.method == 'POST':
        owner = request.POST.get("owner")
        book = request.POST.get("book")

        new_book = SavedBook(owner=owner, book=book)
        new_book.save()
        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def view_profile(request):
    current_profile = Profile.objects.get(user=request.user)
    saved = SavedBook.objects.filter(owner=request.user)
    context = {'profile':current_profile,'saved':saved}
    return render(request, "profile.html", context)

def get_profile_json(request):
    profiles = Profile.objects.get(user=request.user)
    return HttpResponse(serializers.serialize('json',profiles))

@csrf_exempt
def edit_profile_ajax(request):
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
        return HttpResponse("Profile Updated", status=200)
    
    return HttpResponseNotFound()
