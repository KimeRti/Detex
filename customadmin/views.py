from django.shortcuts import render,redirect
from main.models import *
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.models import User
from .forms import UpdateUserForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import *


@login_required(login_url="signin")
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
    
@login_required(login_url="signin")
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
    
@login_required(login_url="signin")
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
    
@login_required(login_url="signin")
def addproduct(request):
    if request.user.is_superuser == 1:
        form = ProductForm()
        if request.method == 'POST':
            form = ProductForm(request.POST)
            if form.is_valid():
                form.save()
                form = ProductForm()
            else:
                form = ProductForm()
                return render(request,"admin/addproduct.html",{"error":"Ürün Eklenirken Bir Hata Oluştu !","form":form})
        return render(request,"admin/addproduct.html",{"form":form,"url":"products"})
    else:
        return redirect('/')
    
@login_required(login_url="signin")
def addcategory(request):
    if request.user.is_superuser == 1:
        form = CategoryForm()
        data = {
            "url":"categories",
            "form":form
        }
        if request.method == 'POST':
            form = CategoryForm(request.POST)
            if form.is_valid():
                form.save()
                form = CategoryForm()
            else:
                form = ProductForm()
                return render(request,"admin/addcategory.html",{"error":"Kategori Eklenirken Bir Hata Oluştu !"},data)
        return render(request,"admin/addcategory.html",data)
    else:
        return redirect('/')
    
@login_required(login_url="signin")
def editproduct(request,pk):
    if request.user.is_superuser == 1:
        product = Product.objects.get(id=pk)
        form = ProductForm(instance=product)
        if request.method == 'POST':
            form = ProductForm(request.POST,instance=product)
            if form.is_valid():
                product_name = form.cleaned_data.get('product_name')
                description = form.cleaned_data.get('description')
                homepage = form.cleaned_data.get('homepage')
                #category = form.changed_data.get('category')
                if product_name == "":
                    product_name = product.product_name
                if description == "":
                    description = product.description
                product.product_name = product_name
                product.description = description
                product.homepage = homepage
                #product.category = category
                form.save()
                form = ProductForm(instance=product)
            else:
                return render(request,"admin/editproduct.html",{'error':'Ürün Güncellenirken Bir Hata Oluştu','form':form})
        return render(request,"admin/editproduct.html",{"form":form})
    else:
        return redirect('/')
    
@login_required(login_url="signin")
def editcategory(request,pk):
    if request.user.is_superuser == 1:
        category = Category.objects.get(id=pk)
        data = {
            "category":category,
            "url":"products"
        }
        if request.method == "POST":
            name = request.POST.get('name')
            parent = request.POST.get('parent')
            if name is None or name == "":
                return render(request,"admin/editcategory.html",{
                    "error":"Kategori Adı Boş Olamaz!",
                    "category":category,
                    "url":"products"})
            if parent is None or parent == "":
                return render(request,"admin/editcategory.html",{
                    "error":"Parent Boş Olamaz!",
                    "category":category,
                    "url":"products"})
            category.name = name
            category.parent = parent
            category.save()
            return redirect('editcategory',pk)

        return render(request,"admin/editcategory.html",data)
    else:
        return redirect('/')
    
@login_required(login_url="signin")
@user_passes_test(lambda u: u.is_superuser)
def deleteproduct(request,pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return redirect('adminproducts')

@login_required(login_url="signin")
@user_passes_test(lambda u: u.is_superuser)
def deletecategory(request,pk):
    category = Category.objects.get(id=pk)
    category.delete()
    return redirect('categories')

@login_required(login_url="signin")
@user_passes_test(lambda u: u.is_superuser)
def listproduct(request,pk):
    category = Category.objects.get(id=pk)
    products = Product.objects.filter(category=category)
    data = {
        "product":products,
        "category":category
    }
    return render(request,"admin/listproducts.html",data)

@login_required(login_url="signin")
@user_passes_test(lambda u: u.is_superuser)
def message(request):
    users = User.objects.all()
    data={
        "users":users,
        "url":"messages"
    }
    return render(request,"admin/message.html",data)

@login_required(login_url="signin")
@user_passes_test(lambda u: u.is_superuser)
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

@login_required(login_url="signin")
@user_passes_test(lambda u: u.is_superuser)
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
