from django.contrib import admin
from django.urls import path,include
from organs import views


admin.site.site_header = "We'll Scan Admin"  
admin.site.site_title = "We'll Scan"
admin.site.index_title = "Welcome to We'll Scan admin panel "


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('organs.urls')),
    path('login/',views.LoginPage,name='login'),
    
    path('signup/',views.SignupPage,name='signup'),
]
