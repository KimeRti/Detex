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
    photo1 = models.ImageField(verbose_name='Ürün Fotoğrafı1',null=True)
    photo2 = models.ImageField(verbose_name='Ürün Fotoğrafı2',null=True)
    photo3 = models.ImageField(verbose_name='Ürün Fotoğrafı3',null=True)
    photo4 = models.ImageField(verbose_name='Ürün Fotoğrafı4',null=True)
    photo5 = models.ImageField(verbose_name='Ürün Fotoğrafı5',null=True)
    photo6 = models.ImageField(verbose_name='Ürün Fotoğrafı6',null=True)
    photo7 = models.ImageField(verbose_name='Ürün Fotoğrafı7',null=True)
    photo8 = models.ImageField(verbose_name='Ürün Fotoğrafı8',null=True)
    photo9 = models.ImageField(verbose_name='Ürün Fotoğrafı9',null=True)
    photo10 = models.ImageField(verbose_name='Ürün Fotoğrafı10',null=True)
    homepage = models.BooleanField(default=False,verbose_name='Anasayfada Gözüksün')
    category = models.ManyToManyField(Category,null=True)
    def __str__(self):
        return self.product_name
