from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.forms import CheckboxInput, ChoiceField, EmailInput, NumberInput, Select,TextInput, Textarea
from main.views import *
from main.models import Product,Category


class UpdateUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username','email' )
        widgets = {
            'username':TextInput(attrs={'class': 'input','placeholder':'username'}),
            'email':EmailInput(attrs={'class':'input','placeholder':'email'}),
        }
        
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name','description','category','homepage','photo')
        widgets = {
            'product_name':TextInput(attrs={'class':'form-control bg-dark','palaceholder':'Ürün Adı'}),
            'description':Textarea(attrs={'class':'form-control','palaceholder':'Ürün Açıklaması','name':'description'}),
            'homepage':CheckboxInput(attrs={'class':'form-check-input','palaceholder':'Ürün Adı'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name':TextInput(attrs={'class':'form-control bg-dark','palaceholder':'Kategori Adı'}),
            'parent':NumberInput(attrs={'class':'form-control bg-dark','palaceholder':'Kategori Parentı'}),
        }
   

