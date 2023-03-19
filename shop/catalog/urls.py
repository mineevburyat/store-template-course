from django.contrib import admin
from django.urls import path
from .views import products, add_to_basket

app_name='product'

urlpatterns = [
    path('', products, name='index'),
    path('product/add/<int:product_id>', add_to_basket, name='add_product'),
]