from django.contrib import admin
from .models import Book, LikedBook, SavedBook
# Register your models here.
admin.site.register(Book)
admin.site.register(SavedBook)
admin.site.register(LikedBook)
