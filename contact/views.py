from django.shortcuts import render , redirect
from .models import Contact
# Create your views here.
def submit(request):
    context = {
        'contact_page':'active'
    }
    return render(request , 'contact.html',context)

def query(request):
    if request.method  == 'POST':
        Name = request.POST['name']
        Email = request.POST['email']
        Subject = request.POST['subject']
        Message = request.POST['message']

        query = Contact.objects.create(Name=Name , Email=Email , Subject=Subject , Message=Message)
        return redirect('/thankyou')

