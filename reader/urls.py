from django.urls import path
from . import views

app_name = 'reader'

urlpatterns = [
    path('mytbr', views.show_saved, name='show_saved'),
    path('create_ajax', views.create_ajax, name='create_ajax'),
    path('profile', views.view_profile, name='view_profile'),
    path('get_profile_json',views.get_profile_json,name='get_profile_json'),
    path('edit_profile_ajax',views.edit_profile_ajax,name='edit_profile_ajax')
]