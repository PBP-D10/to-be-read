from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['ISBN', 'title', 'author', 'year', 'publisher', 'image_s', 'image_m', 'image_l']
