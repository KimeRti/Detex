from django.contrib import messages
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from .token import account_activation_token


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


account_activation_token: object = default_token_generator


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
    user = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = user.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'account/email.html', {"success": "Hesabınız başarıyla aktif edildi. Giriş yapabilirsiniz.", "active": True})
    else:
        return render(request, 'account/email.html', {"error": "Aktivasyon linki geçersiz!", 'errorr': True})


def account(requset):
    if requset.user.is_authenticated:
        return render(requset, 'account/account.html',{'url': 'account'})
    else:
        return render(requset, 'main/404.html')

def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(email=data)
            if associated_users.exists():
                for user in associated_users:
                    current_site = get_current_site(request)
                    subject = 'Şifre Sıfırlama Talebi'
                    message = render_to_string('account/pass_reset_email.html', {
                        'user': user,
                        'domain': current_site.domain,
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': default_token_generator.make_token(user),
                    })
                    user.email_user(subject, message)
                return render(request,'account/password_reset_done.html')
            else:
                messages.error(request, 'Bu email ile kayıtlı kullanıcı bulunamadı.')
    else:
        password_reset_form = PasswordResetForm()
    return render(request=request, template_name='account/password_reset.html', context={'password_reset_form': password_reset_form})


def logout_request(request):
    logout(request)
    return redirect('/')


