from django.contrib import admin
from django.urls import path
from django.conf.urls import  url

from . import views
app_name='accounts'

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile , name='profile'),
    path('update', views.update , name='update'),
    path('notification' , views.notification , name='notification'),
]