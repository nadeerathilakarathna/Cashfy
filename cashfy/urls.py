from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('/geticons', views.geticons, name='geticons'),
    path('getaccounts', views.getaccounts, name='getaccounts'),
]
