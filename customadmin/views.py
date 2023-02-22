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
def addcategory(request):
    if request.user.is_superuser == 1:
        data = {
            "url":"categories"
        }
        return render(request,"admin/addcategory.html",data)
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
    
@login_required(login_url="login")
def editcategory(request,pk):
    if request.user.is_superuser == 1:
        category = Category.objects.get(id=pk)
        data = {
            "category":category,
            "url":"products"
        }
        return render(request,"admin/editcategory.html",data)
    else:
        return redirect('/')
    
def deleteproduct(request,pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return redirect('adminproducts')

def deletecategory(request,pk):
    category = Category.objects.get(id=pk)
    category.delete()
    return redirect('admincategory')

@login_required(login_url="login")
def listproduct(request,pk):
    category = Category.objects.get(id=pk)
    products = Product.objects.filter(category=category)
    data = {
        "product":products,
        "category":category
    }
    return render(request,"admin/listproducts.html",data)
