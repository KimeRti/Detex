from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('aadmin/', admin.site.urls),
    path('admin/',include('customadmin.urls')),
    path('',include('main.urls')),
    path('chat/',include('chat.urls')),
    path('account/',include('account.urls'))
]
