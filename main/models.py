from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.CharField(max_length=10)
    def __str__(self):
        return self.name
    def get_name(self):
        return self.name

class Product(models.Model):
    product_name = models.CharField(max_length=200,verbose_name='Ürün Adı')
    description = models.TextField(verbose_name='Ürün Açıklaması')
    photo = models.ImageField(verbose_name='Ürün Fotoğrafı',null=True)
    homepage = models.BooleanField(default=False,verbose_name='Anasayfada Gözüksün')
    category = models.ManyToManyField(Category,null=True)
    def __str__(self):
        return self.product_name
    
