import json
from django.shortcuts import render, redirect
from book.models import Book
from .forms import BookForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

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
        return redirect('book:Home')

    except Exception as e:
        print("Exception type:", type(e))
        print("Exception message:", str(e))
        return JsonResponse({"error": str(e)}, status=500)

@csrf_exempt
def create_book_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_book = Book.objects.create(
            user = request.user,
            ISBN = data["fields"]["ISBN"],
            title = data["fields"]["title"],
            author = data["fields"]["author"],
            year = int(data["fields"]["year"]),
            pubslisher = data["fields"]["publisher"],
            image_s = data["fields"]["image_s"],
            image_m = data["fields"]["image_m"],
            image_l = data["fields"]["image_l"],
        )

        new_book.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)