from django.urls import path
from . import views

app_name = 'reader'

urlpatterns = [
    path('mytbr', views.show_saved, name='show_saved'),
    path('create_ajax', views.create_ajax, name='create_ajax'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
    path('profile', views.view_profile, name='view_profile'),
    path('mytbr/<int:book_id>/', views.saved_detail, name='saved_detail'),
    path('create-quote/', views.create_quote, name='create_quote'),
    path('get-quote/', views.get_quote_json, name='get_quote_json'),
]