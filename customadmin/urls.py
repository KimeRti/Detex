from django.urls import path
from . import views
from django.conf.urls import handler404

urlpatterns = [
    path("",views.adminpanelproducts,name="adminproducts"),
    path("categories",views.adminpanelcategory,name="categories"),
    path("users",views.adminpanelusers,name="users"),
    path("addproduct",views.addproduct,name="addproduct"),
    path("editproduct/<int:pk>",views.editproduct,name="editproduct")
]
handler404="main.views.handle_not_found"