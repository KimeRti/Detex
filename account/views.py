from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash, get_user_model
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from main.models import Product

from .token import account_activation_token
from pprint import pprint


def signin(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is None:
            return render(request, 'account/signin.html',{'error':'kullanıcı adı veya şifre hatalı'})
        else:
            login(request, user)
            return redirect('home')
            
    return render(request, "account/signin.html")


def signup(request):
    if request.user.is_authenticated:
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
                return render(request, "account/signup.html", {"error": "Bu kullanıcı adı daha önceden alınmış lütfen farklı bir kullanıcı adı giriniz", "firstname": FormFirstName, "lastname": FormLastName, "email": Formemail})
            else:
                if User.objects.filter(email=Formemail).exists():
                    return render(request,"account/signup.html", {"error": "Bu email ile daha önceden kayıt olunmuş!", "username":Formusername, "firstname": FormFirstName, "lastname": FormLastName})
                else: 
                    user = User.objects.create_user(first_name=FormFirstName, last_name=FormLastName, username=Formusername, email=Formemail, password=Formpassword, is_superuser=0, is_active=0)
                    user.save()
                    current_site = get_current_site(request)
                    mail_subject = 'Hesabınızı aktifleştirin.'
                    message = render_to_string('account/acc_active_email.html', {
                        'user': user,
                        'domain': current_site.domain,
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': account_activation_token.make_token(user),
                    })
                    to_email = Formemail
                    email = EmailMessage(
                                mail_subject, message, to=[to_email]
                    )
                    email.send()
                    return render(request, "account/email.html", {"success": "Aktivasyon linki mailinize gönderildi."})
        else:
            return render(request, "account/signup.html", {"error": "Şifreler eşleşmiyor!"})
    return render(request, "account/signup.html")


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        pprint(user)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'account/email.html', {"success": "Hesabınız başarıyla aktif edildi. Giriş yapabilirsiniz.", "active": True})
    else:
        return render(request, 'account/email.html', {"error": "Aktivasyon linki geçersiz!", 'errorr': True})


def logout_request(request):
    logout(request)
    return redirect('/')


