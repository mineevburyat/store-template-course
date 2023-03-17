from django.shortcuts import render, HttpResponse
from .models import Product, ProductCategory

# Create your views here.
def index(request):
    return render(request, 'catalog/index.html', context={
        'title': 'Store - магазин',
    })

db = [
            {'img': 'vendor/img/products/Adidas-hoodie.png',
             'name': 'Худи черного цвета с монограммами adidas Originals',
             'price': 6090.00,
             'descript': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
             },
            {'img': 'vendor/img/products/Blue-jacket-The-North-Face.png',
             'name': 'Синяя куртка The North Face',
             'price': 23725.00,
             'descript': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
             },
            {'img': 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
             'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
             'price': 3390.00,
             'descript': 'Материал с плюшевой текстурой. Удобный и мягкий.',
             },
            {'img': 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
             'name': 'Черный рюкзак Nike Heritage',
             'price': 2340.00,
             'descript': 'Плотная ткань. Легкий материал.',
             },
            {'img': 'vendor/img/products/Black-Dr-Martens-shoes.png',
             'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
             'price': 13590.00,
             'descript': 'Гладкий кожаный верх. Натуральный материал.',
             },
            {'img': 'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png',
             'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
             'price': 2890.00,
             'descript': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
             },
        ]

def products(request):
    return render(request, 'catalog/products.html', context={
        'title': 'Store - продукты',
        'products': Product.objects.all(),
        'category': ProductCategory.objects.all()
    })
