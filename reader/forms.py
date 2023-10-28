from django import forms
from django.forms import ModelForm
from book.models import SavedBook, Book

# class SavedForm(ModelForm):
#     class Meta:
#         model = Book
#         fields = forms.ChoiceField(choices=[('date_added', 'date_added'), ('title', 'title')])


class SavedForm(forms.Form):
    selected_value = forms.ChoiceField(choices=[('date_added', 'date added'), ('book__title', 'title')])
