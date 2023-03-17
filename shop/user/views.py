from django.shortcuts import render, HttpResponseRedirect
from .forms import FormAuth
from django.contrib.auth import authenticate
from django.urls import reverse

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = FormAuth(request.POST)
        if form.is_valid:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                return HttpResponseRedirect(reverse('index'))
    else:
        form = FormAuth()
    return render(request, 
                  'user/login.html',
                  context={
                      'form': form,
                  })

def register_user(request):
    return render(request, 'user/register.html')

def profile(request):
    return render(request, 'user/profile.html')