from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
      path('', views.homepage, name='home'),
    path('appointment/', views.appointment, name='appointment'),
    path('appointment/success/', views.appointment_success, name='appointment_success'),
    path('navbar/', views.navbar, name='navbar'),
    path('login/', views.login_user, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_user, name='logout'),
    path('login_data/', views.login_user_ser, name='login data'),
    path('signup_data/', views.signup_user_ser, name='signup data'),
]
