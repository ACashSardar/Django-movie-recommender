from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from . forms import UserRegistrationFrom
from django import forms
from django.contrib.auth import authenticate,login as UserLogin,logout as UserLogout
from django.contrib.auth import views as auth_views
from recommender.views import home

# Create your views here.
LoggedIn=False
def isLoggedIn():
    global LoggedIn
    return LoggedIn

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            UserLogin(request,user)
            global LoggedIn
            LoggedIn=True
            print('USER ADDED')
            return home(request)
    return render(request,'login.html')


def register(request):
    if request.method=='POST':
        form=UserRegistrationFrom(request.POST)
        if form.is_valid():
            form.save()
            # username=form.cleaned_data.get('username')
            return redirect('login')
    else:
        print('Message Display2')
        form=UserRegistrationFrom()

    return render(request,'register.html',{'form':form})


def logout(request):
    global LoggedIn
    LoggedIn=False
    UserLogout(request)
    return render(request,'logout.html')