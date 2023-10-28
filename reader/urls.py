from django.urls import path
from . import views
#from book import Book

app_name = 'reader'

urlpatterns = [
    path('mytbr', views.show_saved, name='show_saved'),
    path('create_ajax', views.create_ajax, name='create_ajax'),
    path('profile', views.view_profile, name='view_profile'),
    path('mytbr/<int:book_id>/', views.saved_detail, name='saved_detail'),
    path('get_profile_json',views.get_profile_json,name='get_profile_json'),
    path('get_savedBook_json',views.get_savedBook_json,name='get_savedBook_json'),
    path('edit_profile_ajax',views.edit_profile_ajax,name='edit_profile_ajax'),
]