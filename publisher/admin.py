from django.contrib import admin
from .models import Publisher, PublisherHouse

# Register your models here.
admin.site.register(Publisher)
admin.site.register(PublisherHouse)