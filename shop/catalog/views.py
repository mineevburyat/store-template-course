from django.shortcuts import render, HttpResponse
from .models import Product, ProductCategory

# Create your views here.
def index(request):
    return render(request, 'catalog/index.html', context={
        'title': 'Store - магазин',
    })

def products(request):
    return render(request, 'catalog/products.html', context={
        'title': 'Store - продукты',
        'products': Product.objects.all(),
        'category': ProductCategory.objects.all()
    })
