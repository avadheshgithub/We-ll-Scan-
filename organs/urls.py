from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.index, name='index'),
    path('contact',views.contact, name='contact'),
    path('diet',views.diet,name='diet'),
    path('about',views.about,name='about'),

    path('heart',views.heart,name='heart'),
    path('kidney',views.kidney,name='kidney'),
    path('diebetes',views.diebetes,name='diebetes'),

    path('heartresult',views.heartresult,name='heartresult'),
    path('kidneyresult',views.kidneyresult,name='kidneyresult'),
    path('diebetesresult',views.diebetesresult,name='diebetesresult'),

    path('bmicalc',views.bmicalc,name='bmicalc'),

    path('team',views.team, name='team'),

    path('login',views.login, name='login'),

    path('main',views.main, name='main')



    
    # path('signup', views.handleSignUp, name='handleSignUp'),
    # path('login',views.login,name='handlelogin'),
    # path('logout',views.logout,name='handlelogout'),
]
