from django.urls import path
from . import views

urlpatterns =[
    path('',views.firstpage,name='firstpage'),
    path('homepage',views.home,name='home'),
    path('output',views.output,name='output'),
]