from django.contrib.auth.decorators import login_required
# from django.core.paginator import Paginator
from django.shortcuts import HttpResponseRedirect, get_object_or_404
# from django.urls import reverse_lazy
from django.views.generic import ListView
# from django.views.generic.edit import DeleteView
# from user.models import User

from .models import Basket, Product, ProductCategory
from common.mixins import TitleMixin, CategoryMixin


class ProductsListView(TitleMixin, CategoryMixin, ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'catalog/products.html'
    paginate_by = 3
    title = 'Mагазин Store - товары'
    category = ProductCategory.objects.all()

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        if category_id:
            category = get_object_or_404(ProductCategory, id=category_id)
            products = Product.objects.filter(category=category)
        else:
            products = Product.objects.all()
        return products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_id'] = self.kwargs.get('category_id')
        return context


@login_required
def add_to_basket(request, product_id):
    user = request.user
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
    user = request.user
    product = Product.objects.get(id=product_id)
    Basket.objects.filter(user=user, product=product).delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
