from django.shortcuts import render , get_object_or_404
from shop.models import  Product

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import  View
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import  messages
from django.shortcuts import  redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
def cart(request):
    
   
    return render(request , 'cart.html')





def add_to_cart(request , slug):
   return render(request , 'cart.html')