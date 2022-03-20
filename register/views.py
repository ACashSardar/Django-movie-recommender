from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . forms import UserRegistrationFrom
from django import forms
from django.contrib.auth import views as auth_views

# Create your views here.

def login(request):
    login_view=auth_views.LoginView.as_view(template_name='login.html')(request)
    if request.method=='POST':
        try:
            username=request.POST['username']
            print(username)
            messages.success(request, f'Hi👋 {username}!')
            return render(request,'homepage.html')
        except:
            return login_view
    return login_view

def register(request):
    if request.method=='POST':
        form=UserRegistrationFrom(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'Hi👋 {username}!')
            return redirect('login')
    else:
        print('Message Display2')
        form=UserRegistrationFrom()

    return render(request,'register.html',{'form':form})