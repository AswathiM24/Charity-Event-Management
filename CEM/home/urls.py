#from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.homepage,name='landing_page'),
    path('order',views.new_order,name='create_order'),
    path('paymenthandler',views.paymenthandler,name='paymenthandler')
    
]
