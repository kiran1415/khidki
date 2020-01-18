from django.shortcuts import render

# Create your views here.
#def default(request):


def index(request):
    return render(request , 'index.html')
def view_404(request):
    return  render(request , '404.html')
def home(request):
    return render(request , 'home.html')
def about(request):
    return render(request , 'about.html')

def tracking(request):
    return render(request , 'tracking.html')