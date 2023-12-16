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
    path('get_savedBook_json/',views.get_savedBook_json,name='get_savedBook_json'),
    path('edit_profile_ajax',views.edit_profile_ajax,name='edit_profile_ajax'),
    path('create-quote-flutter/', views.create_quote_flutter, name='create_quote_flutter'),
    path('book_by_id/<int:id>/', views.show_json_by_id, name='book_by_id/'),
    path('create-saved-flutter/', views.create_saved_flutter, name='create-saved-flutter/')
]