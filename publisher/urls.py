from django.urls import path
from .views import get_publisher_house, houses

urlpatterns = [
    path('houses/', houses, name='houses'),
    path('get-houses/', get_publisher_house, name='get_publisher_houses')
]
