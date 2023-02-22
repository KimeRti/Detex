from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.forms import EmailInput,TextInput


class UpdateUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username','email' )
        widgets = {
            'username':TextInput(attrs={'class': 'input','placeholder':'username'}),
            'email':EmailInput(attrs={'class':'input','placeholder':'email'}),
        }
   

