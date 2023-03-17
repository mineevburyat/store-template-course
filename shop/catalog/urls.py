from django.contrib import admin
from django.urls import path
from .views import products

app_name='product'

urlpatterns = [
    path('', products, name='index')
]