from django.http import *
from .models import Publisher

def publisher_required(view_func):
    def wrapped_view(request, *args, **kwargs):
        try:
            publisher = Publisher.objects.get(user=request.user)
        except Publisher.DoesNotExist:
            return HttpResponse("<script>alert('This access is only for publishers');</script>")

        return view_func(request, *args, **kwargs)
    
    return wrapped_view
