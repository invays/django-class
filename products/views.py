from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'products/index.html')


def products(request):
    return render(request, 'products/products.html')

