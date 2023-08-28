from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import User_Registration, Login
from django.contrib.auth.models import auth
from django.contrib.auth import get_user_model
from django.contrib import messages

User = get_user_model()

# Create your views here.
def register(request, *args, **kwargs):
    form = User_Registration(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
                                    
        user = User.objects.create_user(username = username, email = email,password = password,first_name=first_name,last_name=last_name)
        user.save()
        
#        messages.success(request,'Registration was successful')
        return redirect('/')

    return render(request, 'registration.html',{'form':form})

def login(request, *args, **kwargs):
    form = Login(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = auth.authenticate(username=username, password=password)
        if user != None:
            auth.login(request,user)
            #messages.success(request,'login successful')
            return redirect('/')
    #messages.warning(request,'login failed: invalid username or password')
    return render(request, 'login.html',{'form':form})


def logout(request):
    auth.logout(request)
    return redirect('/')