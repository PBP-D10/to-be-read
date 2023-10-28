from django.db import models
from django.contrib.auth.models import User

# Create your models here.
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
