from django.shortcuts import render,redirect
from main.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UpdateUserForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages


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

        if request.method == "POST":
            product_name = request.POST.get('product_name')
            product_description = request.POST.get('description')
            product_category = request.POST.get('category')
            photo1 = request.POST.get('photo1')
            product = Product.objects.create(product_name=product_name,description=product_description,photo1=photo1)
            product.save()
            product.category.set(product_category)
            return redirect('adminproducts')

        return render(request,"admin/addproduct.html",data)
    else:
        return redirect('/')
    
@login_required(login_url="login")
def addcategory(request):
    if request.user.is_superuser == 1:
        data = {
            "url":"categories"
        }
        if request.method == "POST":
            category_name = request.POST.get('name')
            parent = request.POST.get('parent')
            category = Category.objects.create(name=category_name,parent=parent)
            category.save()
            return redirect('categories')
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
    return redirect('categories')

@login_required(login_url="login")
def listproduct(request,pk):
    category = Category.objects.get(id=pk)
    products = Product.objects.filter(category=category)
    data = {
        "product":products,
        "category":category
    }
    return render(request,"admin/listproducts.html",data)

@login_required(login_url="login")
def message(request):
    users = User.objects.all()
    data={
        "users":users,
        "url":"messages"
    }
    return render(request,"admin/message.html",data)

@login_required(login_url="login")
def account(request):
    user_form = UpdateUserForm(request.POST, instance=request.user)
    if request.method == 'POST':
        if user_form.is_valid():
            username = user_form.cleaned_data.get("username")
            email = user_form.cleaned_data.get("email")
            if username is None or username == "":
                username = request.user.username
            if email is None or email == "":
                email = request.user.email
            user = User.objects.get(username=request.user.username)
            user.username = username
            user.email = email
            user.save()
        return redirect('profile')
    return render(request,"admin/profile.html",{"user_form":user_form})

@login_required(login_url="login")
def changepass(request):
    if request.user.is_superuser == True:
        if request.method == "POST":
            form = PasswordChangeForm(request.user,request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request,user)
                messages.success(request,'Şifreniz Başarıyla Güncellendi')
                return redirect('account')
            else:
                return render(request,"admin/changepass.html",{"password_incorrect":"Your old password was entered incorrectly. Please enter it again."})
        else:
            form = PasswordChangeForm(request.user)
            return render(request,"admin/changepass.html",{
                'form': form
            })
    return redirect('/home')
