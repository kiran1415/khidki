

# Create your views here.
#def login(request):
 #   return render(request , 'login.html')

#def logout(request):
 #   pass

#def register(request):
 #   return render(request , 'register.html')



from django.conf import  settings
from django.shortcuts import render , redirect
from django.contrib.auth.models import User , auth
from django.contrib import messages
from  django.core import mail
from  django.core.mail import send_mail
from .models import Profile
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name=request.POST['FirstName']
        last_name=request.POST['LastName']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        
        if pass1 == pass2:
            if User.objects.filter(username=email).exists():
                messages.warning(request , 'email is already registered')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.warning(request , 'email is already registered')
                return redirect('/')
        
            else:
                 user = User.objects.create_user(username = email,password = pass1 , first_name=first_name , last_name=last_name ,   email=email)
                 user.save();
                 return redirect('/')
        else:
             messages.warning(request , 'password does not metch')
             return redirect('/') 
    else:
        return redirect('/')




def login(request):
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['password']
         
        user = auth.authenticate(username = username , password = password)

        if user is not None:
            auth.login( request, user)
            return redirect('/')
        else:
            messages.warning(request , 'Please Enter Valid Username And Password')
            return redirect('/')
    else:
        return redirect('/')

def logout(request):
    auth.logout(request)
    return redirect('/')
@login_required(login_url='')
def profile(request):
    return render(request , 'profile.html')

def notification(request):
    return render(request , 'notification.html')

def update(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['first_name']
        Email= request.POST['first_name']
        Mobile_no = request.POST['first_name']
        City = request.POST['City']
        ba = request.POST['ba']
        sa = request.POST['sa']


      