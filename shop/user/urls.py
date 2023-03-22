from django.contrib import admin
from django.urls import path
from .views import register_user, profile, AuthView, MyLogoutView


app_name='user'

urlpatterns = [
    # path('logout', products, name='index'),
    path('login', AuthView.as_view(), name='login'),
    path('register', register_user, name='register'),
    path('profile', profile, name='profile'),
    path('logout', MyLogoutView.as_view(), name='logout'),
]