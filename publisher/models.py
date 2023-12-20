from typing import Any
from django.db import models
from django.contrib.auth.models import User


class PublisherHouse(models.Model):
    name = models.CharField(max_length=255)
    year_established = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

class Publisher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    publisher_house = models.ForeignKey(PublisherHouse, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

