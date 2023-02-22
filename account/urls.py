from django.urls import path
from . import views
from django.conf.urls import handler404

urlpatterns = [
    path("signin",views.signin,name="signin"),
    path("signup",views.signup,name="signup"),
    path("logout",views.logout_request,name="logout"),
]
handler404="main.views.handle_not_found"




