from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):

     search_fields = ['product_name']

     class Meta:
         model = Product


admin.site.register(Product, PostAdmin),
admin.site.register(Category),
admin.site.register(SubCategory),