from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404

urlpatterns = [
    path('aadmin/', admin.site.urls),
    path('admin/',include('customadmin.urls')),
    path('',include('main.urls')),
    path('chat/',include('chat.urls')),
    path('account/',include('account.urls'))
]
handler404="main.views.handle_not_found"

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
