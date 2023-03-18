from django.contrib.auth.forms import AuthenticationForm, \
                                        UserCreationForm, \
                                        UserChangeForm
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
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control py-4',
            'placeholder': 'Введите имя'
        }
    ))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control py-4',
            'placeholder': 'Введите фамилию'
        }
    ))
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control py-4',
            'placeholder': 'Введите имя пользователя',
            'aria-describedby': "usernameHelp"
        }
    ))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control py-4',
            'placeholder': 'Введите адрес эл. почты',
            'aria-describedby': "emailHelp"
        }
    ))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите пароль'
        }
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
        'class': 'form-control py-4',
        'placeholder': 'Подтвердите пароль'
        }
    ))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', \
            'username', 'email', 'password1', 'password2')
        
class FormChangeProfile(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control py-4',
            
        }
    ))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control py-4',
            
        }
    ))
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control py-4',
            'readonly': True,
            'aria-describedby': "usernameHelp"
        }
    ))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control py-4',
            'readonly': True,
            'aria-describedby': "emailHelp"
        }),
        required=False)
    image = forms.ImageField(widget=forms.FileInput(
        attrs= {
            'class': 'custom-file-input',
            'size': '50',
        }),
        required=False)
    
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', \
            'username', 'email', 'image',)