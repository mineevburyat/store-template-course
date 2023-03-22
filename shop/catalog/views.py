from django.shortcuts import render, HttpResponseRedirect
from .models import Product, ProductCategory, Basket
from user.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.views.generic import ListView

# Create your views here.
# def index(request):
#     return render(request, 'catalog/index.html', context={
#         'title': 'Store - магазин',
#     })

class ProductsListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'catalog/products.html'
    paginate_by = 3
    
    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        if category_id:
            category = ProductCategory.objects.get(id=category_id)
            products = Product.objects.filter(category=category)
        else:
            products = Product.objects.all()
        return products
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['title'] = 'Mагазин Store - товары'
        context['category'] = ProductCategory.objects.all()
        context['category_id'] = self.kwargs.get('category_id')
        return context

# def products(request, category_id=None):
#     PER_PAGE = 3
#     if category_id:
#         category = ProductCategory.objects.get(id=category_id)
#         products = Product.objects.filter(category=category)
#     else:
#         products = Product.objects.all()
#     page = request.GET.get('page', 1)
#     if not isinstance(page, int):
#         if page.isdigit():
#             page = int(page)
#         else:
#             page = 1
#     paginator = Paginator(products, per_page=PER_PAGE)
#     page_products = paginator.page(page)
#     return render(request, 'catalog/products.html', context={
#         'title': 'Store - продукты',
#         'products': page_products,
#         'category': ProductCategory.objects.all(),
#         'category_id': category_id
#     })

@login_required
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

@login_required
def remove_from_basket(request, product_id):
    user=request.user
    product = Product.objects.get(id=product_id)
    Basket.objects.filter(user=user, product=product).delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])