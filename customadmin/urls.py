from django.urls import path
from . import views
from django.conf.urls import handler404

urlpatterns = [
    path("",views.adminpanelproducts,name="adminproducts"),
    path("categories",views.adminpanelcategory,name="categories"),
    path("users",views.adminpanelusers,name="users"),
    path("addproduct",views.addproduct,name="addproduct"),
    path("addcategory",views.addcategory,name="addcategory"),
    path("editproduct/<int:pk>",views.editproduct,name="editproduct"),
    path("editcategory/<int:pk>",views.editcategory,name="editcategory"),
    path("deleteproduct/<int:pk>",views.deleteproduct,name="deleteproduct"),
    path("deletecategory/<int:pk>",views.deletecategory,name="deletecategory"),
    path("listproducts/<int:pk>",views.listproduct,name="listproducts")
]
handler404="main.views.handle_not_found"