from django.contrib import admin
from django.urls import path
from .views import index, products

urlpatterns = [
    path('', index),
    path('products', products)
]