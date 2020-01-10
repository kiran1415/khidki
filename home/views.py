from django.shortcuts import render

# Create your views here.
#def default(request):
 #   return render(request , 'default.html') 


def index(request):
    return render(request , 'home.html')
