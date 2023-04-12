from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls import handler404

urlpatterns = [
    path("signin", views.signin,name="signin"),
    path("signup", views.signup,name="signup"),
    path("logout", views.logout_request,name="logout"),
    path("activate/<uidb64>/<token>/", views.activate, name='activate'),
    path("password_reset", views.password_reset_request, name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_complete.html'), name='password_reset_confirm'),
]

handler404 = "main.views.handle_not_found"




