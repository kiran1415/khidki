from django.shortcuts import render , get_object_or_404
from shop.models import  Product
from cart.models import  CartItem
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import  View
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import  messages
from django.shortcuts import  redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
def cart(request):
    
    products  = CartItem.objects.all()
    print(products)
    return render(request , 'cart.html' , {'products':products})





def add_to_cart(request , slug):
    product = get_object_or_404(Product , slug=slug )
    #order_item, created = CartItem.objects.get_or_create(
     #   item=item,
      #  user=request.user,

       # ordered=False
    #)
    cart_item , created = CartItem.objects.get_or_create(
        product = product ,
        user   =  request.user ,
        ordered = False
    )