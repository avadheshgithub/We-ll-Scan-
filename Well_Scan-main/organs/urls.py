from django.contrib import admin
from django.urls import path,include
from .import views

    # path('contact/',views.contact, name='contact'),
    # path('diet/',views.diet,name='diet'),
    # path('about/',views.about,name='about'),
    # path('signup/', views.handleSignUp, name='handleSignUp'),
    # path('login/',views.login,name='login'),
    # path('logout/',views.logout,name='logout'),


urlpatterns = [
    path('', views.index, name='index'), 
    path('team/', views.team, name='team'),
    path('contact/',views.contact, name='contact'),
    path('consultation/',views.consultation, name="consultation"),
    path('diet',views.diet, name='diet'),


    path('heart/',views.heart,name='heart'),
    path('kidney',views.kidney,name='kidney'),
    path('diebetes',views.diebetes,name='diebetes'),
    path('arthritis',views.arthritis, name="arthritis"),

    path('heartresult',views.heartresult,name='heartresult'),
    path('kidneyresult',views.kidneyresult,name='kidneyresult'),
    path('diebetesresult',views.diebetesresult,name='diebetesresult'),
    path('arthritisresult', views.arthritisresult, name="arthritisresult"),
    
    path('login/', views.LoginPage, name="login"),
    path('logout/', views.LogoutPage, name="logout"),  # Ensure this URL is used in the template
    path('signup/', views.SignupPage, name='SignUp'),
 

]
