from django.shortcuts import render, redirect
from book.models import Book
from .forms import BookForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Publisher

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

def check_is_publisher(request):
    publisher = Publisher.objects.filter(user=request.user)
    return JsonResponse({'is_publisher': publisher.exists()})


