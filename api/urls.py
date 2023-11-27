from django.urls import path
from . import views

urlpatterns = [
    # path('', get_books, name='get_books'),
<<<<<<< HEAD
    path('login/', views.login_view, name='Login'),
    path('logout/', views.logout_view, name='Logout'),
    path('register/', views.register_view, name='Register'),
]
=======
    path('login', views.login_view, name='Login'),
    path('logout', views.logout_view, name='Logout'),
    path('register', views.register_view, name='Register'),

    path('login-endpoint', views.login_endpoint, name='Login Endpoint'),
    path('logout-endpoint', views.logout_endpoint, name='Logout Endpoint'),
    path('register-endpoint', views.register_endpoint, name='Register Endpoint'),
]
>>>>>>> 6f35236a40630c588107085f76744a9b8406ac2d
