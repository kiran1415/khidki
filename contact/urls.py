from django.contrib import admin
from django.urls import path


from . import views

app_name = 'contact'

urlpatterns = [
    path('/submit', views.submit, name='submit'),
     path('query', views.query, name='query'),

]