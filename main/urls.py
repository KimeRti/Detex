from django.urls import path
from . import views
from django.conf.urls import handler404

urlpatterns = [
    path('',views.home_view,name="home"),
    path("about", views.about ,name="about"),
    path("contact", views.contact ,name="contact"),
    path("products", views.products ,name="products"),
    path("productdetail<int:pk>",views.productdetail,name="productdetail")
]
handler404="main.views.handle_not_found"




