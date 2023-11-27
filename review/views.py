from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseNotAllowed
from .models import Review
# Create your views here.


@csrf_exempt
def create_review(request):
    if request.method == "POST":
        user = request.user
        book_id = request.POST.get("book_id")
        rating = request.POST.get("rating")
        content = request.POST.get("content")
        new_review = Review.objects.create(
            user=user, book_id=book_id, rating=rating, content=content)
        new_review.save()
        return JsonResponse({
            "status": True,
            "message": "Review berhasil ditambahkan!"
        })
    else:
        return HttpResponseNotAllowed("POST")
