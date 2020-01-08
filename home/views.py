from django.shortcuts import render

# Create your views here.
def default(request):
    return render*request , 'default.html') 


def home(request):
    return render(request , 'index.html')
