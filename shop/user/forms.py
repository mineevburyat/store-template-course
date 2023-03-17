from django.contrib.auth.forms import AuthenticationForm
from .models import User
from django import forms

class FormAuth(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control py-4',
            'plaseholder': 'Введите имя пользователя'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
        'class': 'form-control py-4',
        'plaseholders': 'Введите пароль'
        }
    ))
    class Meta:
        model = User
        fields = ('username', 'password')
        
