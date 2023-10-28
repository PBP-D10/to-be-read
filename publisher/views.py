from django.shortcuts import *
from django.http import *
from .models import Publisher, PublisherHouse, Book
from .forms import BookForm
from django.core import serializers

def get_publisher_house(request):
    publisher_houses = PublisherHouse.objects.all()
    data = [{'name': house.publisher.name, 'year_established': house.year_established} for house in publisher_houses]
    return JsonResponse(data, safe=False)

def houses(request):
    return render(request, 'publisher_house_page.html')
