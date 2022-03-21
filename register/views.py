from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . forms import UserRegistrationFrom
from django import forms
from django.contrib.auth import views as auth_views
from recommender.views import home

# Create your views here.

def login(request):
    try:
        if request.method=='POST':
            username=request.POST['username']
            if str(auth_views.LoginView.as_view(template_name='login.html')(request))[1]=='T':
                return auth_views.LoginView.as_view(template_name='login.html')(request)
        return home(request,username)
        # return render(request,'homepage.html',my_dict)
    except:
        return auth_views.LoginView.as_view(template_name='login.html')(request)

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