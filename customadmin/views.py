from django.shortcuts import render,redirect
from main.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required(login_url="login")
def adminpanelproducts(request):
    if request.user.is_superuser == 1:
        product = Product.objects.all()
        data = {
            "product":product,
            "url":"products"
        }
        return render(request,"admin/products.html",data)
    else:
        return redirect('/')
    
@login_required(login_url="login")
def adminpanelcategory(request):
    if request.user.is_superuser == 1:
        category = Category.objects.all()
        data = {
            "categories":category,
            "url":"category"
        }
        return render(request,"admin/categories.html",data)
    else:
        return redirect('/')
    
@login_required(login_url="login")
def adminpanelusers(request):
    if request.user.is_superuser == 1:
        users = User.objects.all()
        data = {
            "users":users,
            "url":"users"
        }
        return render(request,"admin/users.html",data)
    else:
        return redirect('/')
    
@login_required(login_url="login")
def addproduct(request):
    if request.user.is_superuser == 1:
        category = Category.objects.all()
        data = {
            "categories":category,
            "url":"products"
        }
        return render(request,"admin/addproduct.html",data)
    else:
        return redirect('/')
@login_required(login_url="login")
def editproduct(request,pk):
    if request.user.is_superuser == 1:
        category = Category.objects.all()
        product = Product.objects.get(id=pk)
        data = {
            "categories":category,
            "product":product,
            "url":"products"
        }
        return render(request,"admin/editproduct.html",data)
    else:
        return redirect('/')
def deleteproduct(pk):
    product = Product.delete(id=pk)
    Product.save()
