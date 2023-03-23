from django.shortcuts import render, HttpResponseRedirect
from .forms import FormAuth, FormRegister, FormChangeProfile
from django.contrib import auth, messages
from django.urls import reverse
from catalog.models import Basket
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView, UpdateView
from .models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

class AuthView(LoginView):
    template_name = 'user/login.html'
    authentication_form = FormAuth
    next_page = '/'

class RegisterUserView(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'user/register.html'
    form_class = FormRegister
    success_url = '/user/login'
    success_message = 'успешно зарегестрирован'

class ProfileEditView(UpdateView):
    model = User
    form_class = FormChangeProfile
    template_name = 'user/profile.html'
    success_message = 'профиль изменен'
    
    def get_success_url(self) -> str:
        return reverse_lazy('user:profile', self.object.id)
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['basket'] = Basket.objects.filter(user=self.object)


class MyLogoutView(LogoutView):
    pass
    
