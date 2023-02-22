from django.shortcuts import render
from .models import Product
from django.contrib.auth.models import User

def home_view(request):
    product = Product.objects.filter(homepage=True)
    url='home'
    data = {
        "product":product,
        "url":url
    }
    return render(request,"main/index.html",data)

def about(request):
    url='about'
    data={
        "url":url
    }
    return render(request,"main/about.html",data)

def contact(request):
    url='contact'
    data={
        "url":url
    }
    return render(request,"main/contact.html",data)

def products(request):
    products = Product.objects.all()
    url = 'products'
    data = {
        "product":products,
        "url":url
    }
    return render(request,"main/products.html",data)

def productdetail(request,pk):
    product = Product.objects.get(id=pk)
    url = 'products'
    data = {
        "product":product,
        "url":url
    }
    return render(request,"main/productdetail.html",data)

def handle_not_found(request,exception):
    return render(request,"404.html")
