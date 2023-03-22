from django.shortcuts import render, HttpResponseRedirect
from .forms import FormAuth, FormRegister, FormChangeProfile
from django.contrib import auth, messages
from django.urls import reverse
from catalog.models import Basket
from django.contrib.auth.views import LoginView, LogoutView

class AuthView(LoginView):
    template_name = 'user/login.html'
    authentication_form = FormAuth
    next_page = '/'


def register_user(request):
    if request.method == 'POST':
        form = FormRegister(data=request.POST)
        if form.is_valid():
            messages.success(request, 'успешно зарегестрировались!')
            form.save()
            HttpResponseRedirect(reverse('user:login'))
    else:
        form = FormRegister()
    return render(request, 
                  'user/register.html',
                  context = {
                      'form': form,
                  })

def profile(request):
    if request.method == 'POST' and request.user.is_authenticated:
        form = FormChangeProfile(data=request.POST,
                                instance=request.user,
                                files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user:profile'))
        else:
            pass
            # print(form.errors)
    else:
        if request.user.is_authenticated:
            form = FormChangeProfile(instance=request.user)
        else:
            form = FormChangeProfile()
    basket = Basket.objects.filter(user=request.user)
    
    return render(request, 
                  'user/profile.html', 
                  context={
                    'form': form,
                    'basket': basket,
    })

class MyLogoutView(LogoutView):
    pass
    
