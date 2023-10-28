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
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Publisher(models.Model):
    name = models.CharField(max_length=50, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class PublisherHouse(models.Model):
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    year_established = models.PositiveIntegerField()

    def __str__(self):
        return self.publisher.name
