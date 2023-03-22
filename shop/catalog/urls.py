from django.contrib import admin
from django.urls import path
from .views import add_to_basket, remove_from_basket, ProductsListView

app_name='product'

urlpatterns = [
    path('', ProductsListView.as_view(), name='index'),
    path('category/<int:category_id>', ProductsListView.as_view(), name='category'),
    path('basket/add/<int:product_id>', add_to_basket, name='add_product'),
    path('basket/del/<int:product_id>', remove_from_basket, name='remove_product_from_basket')
]