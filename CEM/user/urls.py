from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('login',views.login,name='user_login'),
    path('signup',views.signup,name='user_signup'),
    path('',views.dashboard,name='user_dashboard'),
    path('organisation',views.organization,name='user_organisation_list'),
    path('logout',views.logout,name='user_logout')
   
    
   
    

]
