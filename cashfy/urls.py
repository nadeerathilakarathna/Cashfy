from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('/geticons', views.geticons, name='geticons'),
    path('getaccounts', views.getaccounts, name='getaccounts'),
    path('createaccount', views.createaccount, name='createaccount'),
    path('getexpenses', views.getexpenses, name='getexpenses'),
    path('createexpense', views.createexpense, name='createexpense'),
    path('getincome', views.getincome, name='getincome'),
    path('createincome', views.createincome, name='createincome'),
    path('createtransaction', views.createtransaction, name='createtransaction'),
]

