from django.urls import path
from . import views

app_name = 'reader'

urlpatterns = [
    path('myprofile/edit', views.edit_profile, name='edit_profile'),
    path('myprofile', views.view_profile, name='view_profile'),
]