# from catalog.models import Basket
# from django.contrib import auth, messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
# from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from .forms import FormAuth, FormChangeProfile, FormRegister
from .models import User
from common.mixins import TitleMixin


class AuthView(TitleMixin, LoginView):
    template_name = 'user/login.html'
    authentication_form = FormAuth
    next_page = '/'
    title = "Магазин Store - Аутентификация"


class RegisterUserView(SuccessMessageMixin, TitleMixin, CreateView):
    model = User
    template_name = 'user/register.html'
    form_class = FormRegister
    success_url = '/user/login'
    success_message = 'успешно зарегестрирован'
    title = "Магазин Store - Регистрация"


class ProfileEditView(TitleMixin, UpdateView):
    model = User
    form_class = FormChangeProfile
    template_name = 'user/profile.html'
    success_message = 'профиль изменен'
    title = "Магазин Store - Профиль"

    def get_success_url(self) -> str:
        return reverse_lazy('user:profile', kwargs={'pk': self.object.id})


class MyLogoutView(LogoutView):
    pass
