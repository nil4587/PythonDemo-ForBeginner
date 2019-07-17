from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.

# /products -> index
# Uniform Resource Locator (Address)


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',
                  {'product_list': products})


def newproduct(request):
    return HttpResponse("New Products")
