from django.contrib.auth.forms import AuthenticationForm, \
                                        UserCreationForm
from .models import User
from django import forms

class FormAuth(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control py-4',
            'placeholder': 'Введите имя пользователя'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите пароль'
        }
    ))
    class Meta:
        model = User
        fields = ('username', 'password')
        

class FormRegister(UserCreationForm):
#     username = forms.CharField(widget=forms.TextInput(
#         attrs={
#             'class': 'form-control py-4',
#             'placeholder': 'Введите имя пользователя'
#         }
#     ))
#     password = forms.CharField(widget=forms.PasswordInput(
#         attrs={
#         'class': 'form-control py-4',
#         'placeholder': 'Введите пароль'
#         }
#     ))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', \
            'username', 'email', 'password1', 'password2')