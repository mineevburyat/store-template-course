from django.shortcuts import render, HttpResponseRedirect
from .forms import FormAuth, FormRegister, FormChangeProfile
from django.contrib import auth
from django.urls import reverse

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = FormAuth(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                print('user not find')
        else:
            print('forms not valid', form, form.errors)
    else:
        form = FormAuth()
    return render(request, 
                  'user/login.html',
                  context={
                      'form': form,
                  })

def register_user(request):
    if request.method == 'POST':
        form = FormRegister(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user:login'))
    else:
        form = FormRegister
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
            print(form.errors)
    else:
        if request.user.is_authenticated:
            form = FormChangeProfile(instance=request.user)
        else:
            form = FormChangeProfile()
    return render(request, 
                  'user/profile.html', 
                  context={
                    'form': form
    })
    
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))