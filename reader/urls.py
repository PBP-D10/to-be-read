from django.urls import path
from . import views

app_name = 'reader'

urlpatterns = [
    path('profile/edit', views.edit_profile, name='edit_profile'),
    path('profile', views.view_profile, name='view_profile'),
]