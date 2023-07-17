from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from account.models import Messages


def home_view(request):
    product = Product.objects.filter(homepage=True)
    url = 'home'
    data = {
        "product": product,
        "url": url
    }
    return render(request, "main/index.html", data)


def about(request):
    url = 'about'
    data = {
        "url": url
    }
    return render(request,"main/about.html",data)


def contact(request):
    url = 'contact'
    data = {
        "url": url
    }
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        name = request.POST.get('name')
        mail = request.POST.get('email')
        messages = Messages.objects.create(subject=subject, message=message, name=name, mail=mail)
        messages.save()
        data = {
            "url": url,
            'success': 'Mesajınız başarıyla gönderildi.'
        }
        return render(request, "main/contact.html", data)
    return render(request, "main/contact.html", data)


def products(request):
    products = Product.objects.all()
    category = Category.objects.all()
    subcategory = SubCategory.objects.all()
    url = 'products'
    data = {
        "product": products,
        "categories": category,
        "url": url,
        "subcategories": subcategory
    }
    return render(request, "main/products.html", data)


def productdetail(request,pk):
    product = Product.objects.get(id=pk)
    url = 'products'
    data = {
        "product": product,
        "url": url
    }
    return render(request, "main/productdetail.html", data)


def handle_not_found(request, exception):
    return render(request, "404.html")
