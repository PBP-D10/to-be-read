from django.urls import path
from . import views

app_name = 'reader'

urlpatterns = [
    path('mytbr', views.show_saved, name='show_saved'),
    path('create_ajax', views.create_ajax, name='create_ajax'),
    path('profile', views.view_profile, name='view_profile'),
    path('mytbr/<int:book_id>/', views.saved_detail, name='saved_detail'),
    path('create-quote/', views.create_quote, name='create_quote'),
    path('get-quote/', views.get_quote_json, name='get_quote_json'),
    path('get_profile_json',views.get_profile_json,name='get_profile_json'),
    path('get_savedBook_json',views.get_savedBook_json,name='get_savedBook_json'),
    path('edit_profile_ajax',views.edit_profile_ajax,name='edit_profile_ajax'),
    path('like_book_ajax',views.like_book_ajax,name='like_book_ajax'),
    path('get_profile_json_flutter',views.get_profile_json_flutter,name='get_profile_json_flutter'),
    path('get_saved_books_json_flutter',views.get_saved_books_json_flutter,name='get_saved_books_json_flutter'),
    path('get_all_profile_json',views.get_all_profile_json,name='get_all_profile_json'),
    path('edit_profile_flutter',views.edit_profile_flutter,name='edit_profile_flutter'),
]