from django.shortcuts import render
from .forms import FormAuth

# Create your views here.
def login(request):
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