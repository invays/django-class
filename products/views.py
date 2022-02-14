from django.shortcuts import render
from django.http import HttpResponse
from .models import ProductCategory, Product


def index(request):
    context = {
        'title': 'geekshop - online store',
        'brand_name': 'Geekshop',
        'catalog_link': 'Каталог',
        'log_in': 'Войти',
        'log_out': 'Выйти',
        'profile': 'Личный кабинет',
        'orders': 'Заказы',
        'admin_panel': 'Админ-панель',
        'header_h1': 'GeekShop магазин',
        'content_body': "Новые образы и лучшие бренды на GeekShop Store.Бесплатная доставка по всему миру! Аутлет: до -70% Собственный бренд. -20% новым покупателям.",
        'products_link': 'Перейти в каталог',
    }
    return render(request, 'products/index.html', context)


def products(request):
    # categories_data = [
    #     {'name': 'Новинки'},
    #     {'name': 'Одежда'},
    #     {'name': 'Обувь'},
    #     {'name': 'Аксессуары'},
    #     {'name': 'Подарки'}
    # ]
    slides_data = [
        {'img': 'vendor/img/slides/slide-1.jpg', 'alt': 'First slide'},
        {'img': 'vendor/img/slides/slide-2.jpg', 'alt': 'Second slide'},
        {'img': 'vendor/img/slides/slide-3.jpg', 'alt': 'Third slide'}
    ]
    # products_data = [
    #     {
    #         'name': 'Худи черного цвета с монограммами adidas Originals',
    #         'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
    #         'price': '6 090,00',
    #         'img': 'vendor/img/products/Adidas-hoodie.png'
    #     },
    #     {
    #         'name': 'Синяя куртка The North Face',
    #         'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
    #         'price': '23 725,00',
    #         'img': 'vendor/img/products/Blue-jacket-The-North-Face.png'
    #     },
    #     {
    #         'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
    #         'description': 'Материал с плюшевой текстурой. Удобный и мягкий.',
    #         'price': '3 390,00',
    #         'img': 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png'
    #     },
    #     {
    #         'name': 'Черный рюкзак Nike Heritage',
    #         'description': 'Плотная ткань. Легкий материал.',
    #         'price': '2 340,00',
    #         'img': 'vendor/img/products/Black-Nike-Heritage-backpack.png'
    #     },
    #     {
    #         'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
    #         'description': 'Гладкий кожаный верх. Натуральный материал.',
    #         'price': '13 590,00',
    #         'img': 'vendor/img/products/Black-Dr-Martens-shoes.png'
    #     },
    #     {
    #         'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
    #         'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
    #         'price': '2 890,00',
    #         'img': 'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png'
    #     },
    # ]
    context = {
        'title': 'Geekshop - Products catalog',
        'brand_name': 'Geekshop',
        'catalog_link': 'Каталог',
        'log_in': 'Войти',
        'log_out': 'Выйти',
        'profile': 'Личный кабинет',
        'orders': 'Заказы',
        'admin_panel': 'Админ-панель',
        'header_h1': 'GeekShop магазин',
        'categories': ProductCategory.objects.all(),
        'slides': slides_data,
        'products': Product.objects.all()
    }
    return render(request, 'products/products.html', context)

