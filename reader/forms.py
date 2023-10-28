from django import forms
from django.forms import ModelForm
from reader.models import Quote

class ItemForm(ModelForm):
    class Meta:
        model = Quote
        fields = ["text"]
