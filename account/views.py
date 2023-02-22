from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout,update_session_auth_hash
from django.contrib import messages
from main.models import Product

def signin(request):
    if request.user.is_authenticated == True:
        return redirect('/')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request,username = username,password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request,"Kullanıcı Adı Veya Şifre Yanlış!")
            return redirect('signin')
            
    return render(request,"account/signin.html")

def signup(request):
    if request.user.is_authenticated == True:
        return redirect('home')
    if request.method == "POST":
        FormFirstName = request.POST.get('firstname')
        FormLastName = request.POST.get('lastname')
        Formusername = request.POST.get('username')
        Formemail = request.POST.get('email')
        Formpassword = request.POST.get('password')
        Formrepassword = request.POST.get('repassword')
        if Formpassword == Formrepassword:
            if User.objects.filter(username=Formusername).exists():
                return render(request,"account/signup.html",{"error":"Bu kullanıcı adı daha önceden alınmış lütfen farklı bir kullanıcı adı giriniz","firstname":FormFirstName,"lastname":FormLastName,"email":Formemail})
            else:
                if User.objects.filter(email=Formemail).exists():
                    return render(request,"account/signup.html",{"error":"Bu email ile daha önceden kayıt olunmuş!","username":Formusername,"firstname":FormFirstName,"lastname":FormLastName})
                else: 
                    user = User.objects.create_user(first_name = FormFirstName,last_name = FormLastName,username=Formusername,email=Formemail,password=Formpassword,is_superuser = 0)
                    user.save()
                    login(request, user)
                    return redirect('home')
        else:
            return render(request,"account/signup.html",{"error":"passwords do not match!"})
    return render(request,"account/signup.html")
        
def logout_request(request):
    logout(request)
    return redirect('/')


