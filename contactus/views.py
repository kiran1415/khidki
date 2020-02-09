from django.shortcuts import render ,  redirect
from .models import Contactus
# Create your views here.
def contact(request):
    return render(request , 'contact.html')

       
       
