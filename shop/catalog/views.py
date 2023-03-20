from django.shortcuts import render, HttpResponseRedirect
from .models import Product, ProductCategory, Basket
from user.models import User
from django.core.paginator import Paginator

# Create your views here.
# def index(request):
#     return render(request, 'catalog/index.html', context={
#         'title': 'Store - магазин',
#     })

def products(request, category_id=None):
    PER_PAGE = 6
    if category_id:
        category = ProductCategory.objects.get(id=category_id)
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()
    page = request.GET.get('page', 1)
    if not isinstance(page, int):
        if page.isdigit():
            page = int(page)
        else:
            page = 1
    paginator = Paginator(products, per_page=PER_PAGE)
    page_products = paginator.page(page)
    return render(request, 'catalog/products.html', context={
        'title': 'Store - продукты',
        'products': page_products,
        'category': ProductCategory.objects.all(),
        'category_id': category_id
    })

def add_to_basket(request, product_id):
    user=request.user
    product = Product.objects.get(id=product_id)
    basket = Basket.objects.filter(user=user, product=product)
    if basket.exists():
        basket = basket.last()
        basket.quantity += 1
        basket.save()
    else:
        if product:
            Basket.objects.create(user=user, product=product, quantity=1)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def remove_from_basket(request, product_id):
    user=request.user
    product = Product.objects.get(id=product_id)
    Basket.objects.filter(user=user, product=product).delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])