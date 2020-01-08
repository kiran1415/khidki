from django.shortcuts import render

# Create your views here.
#def login(request):
 #   return render(request , 'login.html')

#def logout(request):
 #   pass

#def register(request):
 #   return render(request , 'register.html')




from django.shortcuts import render , redirect
from django.contrib.auth.models import User , auth
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name=request.POST['FirstName']
        last_name=request.POST['LastName']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        if pass1 == pass2:
            if User.objects.filter(username=email).exists():
                messages.info(request , 'email is already registered')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request , 'email is already registered')
                return redirect('register')
        
            else:
                 user = User.objects.create_user(username = email,password = pass1 , first_name=first_name , last_name=last_name ,   email=email)
                 user.save();
                 print("user is created")
                 return redirect('register')
        else:
             messages.info(request , 'password does not metch')
             return redirect('register') 
    else:
        return render(request , 'register.html')




def login(request):
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['password']
         
        user = auth.authenticate(username = username , password = password)

        if user is not None:
            auth.login(request,user)
            
            return render(request , 'index.html' )
        else:
            messages.info(request , 'Please Enter Valid Username And Password')
            return render(request , 'login.html')
    else:
        return render(request , 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')