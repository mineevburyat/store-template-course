from django.contrib import admin
from django.urls import path
from .views import login, register_user, profile, logout


app_name='user'

urlpatterns = [
    # path('logout', products, name='index'),
    path('login', login, name='login'),
    path('register', register_user, name='register'),
    path('profile', profile, name='profile'),
    path('logout', logout, name='logout'),
]