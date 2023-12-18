import json
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound, HttpResponse
from book.models import SavedBook, Book, LikedBook
from django.views.decorators.csrf import csrf_exempt
from reader.models import Profile, Quote
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.core import serializers
import json

# Create your views here.


@login_required(login_url='login')
@csrf_exempt
def show_saved(request):
    saved_books = SavedBook.objects.filter(owner=request.user)

    context = {
        'saved_books': saved_books,
    }
    return render(request, "my_tbr.html", context)


@csrf_exempt
def create_ajax(request):
    if request.method == 'POST':
        book_id = request.POST.get("book")

        new_book = SavedBook.objects.get_or_create(
            owner=request.user, book_id=book_id)
        if (new_book[1] == False):
            return HttpResponse(b"ALREADY_EXISTS", status=200)
        else:
            new_book[0].save()
        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()


def view_profile(request):
    current_profile = Profile.objects.get(user=request.user)
    context = {'profile': current_profile}
    return render(request, "profile.html", context)


def get_profile_json(request):
    profile = Profile.objects.get(user=request.user)
    profile_data = {
        "name": profile.name,
        "email": profile.email,
        "address": profile.address,
        "date_of_birth": profile.date_of_birth,
    }
    return JsonResponse(profile_data)


@csrf_exempt
def get_savedBook_json(request):
    savedBook = SavedBook.objects.filter(owner=request.user)
    return HttpResponse(serializers.serialize('json', savedBook), content_type="application/json")


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

        if address == '' or address == '-':
            profile.address = None
        else:
            profile.address = address

        if date_of_birth == '':
            profile.date_of_birth = None
        else:
            profile.date_of_birth = date_of_birth

        profile.save()

        return HttpResponse("Profile Updated", status=200)

    return HttpResponseNotFound()


def saved_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    context = {
        'book': book,
    }
    return render(request, 'saved_detail.html', context=context)


@csrf_exempt
def create_quote(request):
    if request.method == 'POST':
        text = request.POST.get("text")

        new_quote = Quote(text=text)
        new_quote.save()
        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()


def get_quote_json(request):
    quote = Quote.objects.all()
    return HttpResponse(serializers.serialize('json', quote), content_type="application/json")


@csrf_exempt
def create_quote_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)

        new_quote = Quote.objects.create(
            text=data["text"],
        )

        new_quote.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)


def show_json_by_id(request, id):
    data = Book.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


@csrf_exempt
def create_saved_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)

        new_saved = SavedBook.objects.get_or_create(
            owner=request.user,
            book_id=int(data["book"]["pk"]),
        )

        if (new_saved[1] == False):
            return JsonResponse({"status": "already exist"}, status=200)
        
        new_saved[0].save()
        return JsonResponse({"status": "success"}, status=200)
    
    else:
        return JsonResponse({"status": "error"}, status=401)
    
@csrf_exempt
def remove_saved_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)
        deleted_saved = SavedBook.objects.get(
            owner = request.user,
            book_id = int(data["book"]["pk"]),)
        deleted_saved.delete()

        return JsonResponse({"status": "success"}, status=200)

    return JsonResponse({"status": "error"}, status=401)


@csrf_exempt
def like_book_ajax(request):
    if request.method == 'POST':

        data = json.loads(request.body)
        book_id = data.get("book", "")

        print('user: ', request.user)
        print('book_id: ', book_id)

        new_book = LikedBook.objects.get_or_create(
            owner=request.user, book_id=book_id)

        if (new_book[1] == False):
            return JsonResponse({"status": "ALREADY_EXISTS"}, status=200)
        else:
            new_book[0].save()

        return JsonResponse({"status": "created"}, status=200)
    return JsonResponse({"status": "not a post"}, status=200)


@csrf_exempt
def edit_profile_flutter(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        data = json.loads(request.body)

        name = data['name']
        email = data['email']
        address = data['address']
        date_of_birth = data['date_of_birth']

        if name != profile.name:
            profile.name = name
        if email != profile.email:
            profile.email = email

        if address == '' or address == '-':
            profile.address = None
        else:
            profile.address = address

        if date_of_birth == '' or date_of_birth == "null":
            profile.date_of_birth = None
        else:
            profile.date_of_birth = date_of_birth

        profile.save()

        return JsonResponse({"status": "success"}, status=200)

    return JsonResponse({"status": "error"}, status=401)


def get_profile_json_flutter(request):
    profile = Profile.objects.get(user=request.user)
    return HttpResponse(serializers.serialize("json", [profile]), content_type="application/json")


def get_saved_books_json_flutter(request):
    savedBooks = SavedBook.objects.filter(owner=request.user)
    return HttpResponse(serializers.serialize("json", savedBooks), content_type="application/json")


def get_all_profile_json(request):
    profile = Profile.objects.all()
    return HttpResponse(serializers.serialize('json', profile))
