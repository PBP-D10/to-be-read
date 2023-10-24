from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    ISBN = models.CharField(max_length=20, null=True, blank=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    publisher = models.CharField(max_length=50)
    image_s = models.TextField(null=True, blank=True)
    image_m = models.TextField(null=True, blank=True)
    image_l = models.TextField(null=True, blank=True)

class SavedBook(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
