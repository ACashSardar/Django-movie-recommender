from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . forms import UserRegistrationFrom

# Create your views here.

def login(request):
    return render(request,'login.html')

def register(request):

    if request.method=='POST':
        form=UserRegistrationFrom(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'Hi👋 {username}!')
            return redirect('login')
    else:
        form=UserRegistrationFrom()

    return render(request,'register.html',{'form':form})