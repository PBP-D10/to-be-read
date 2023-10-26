from django.urls import path
from . import views

app_name = 'reader'

urlpatterns = [
    path('mytbr', views.show_saved, name='show_saved'),
]