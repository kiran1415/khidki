from django.shortcuts import render
from shop.models import  Product
from shop.models import Category 
from .models import Terms
from django.shortcuts import get_object_or_404
# Create your views here.
#def default(request):


def index(request , category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)[8:11]
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'home_page':'active',
        'category': category,
        'categories': categories,
        'products': products
    }
 

    return render(request , 'index.html', context)

def view_404(request):
    return  render(request , '404.html')

def home(request , category_slug=None):
    return render(request , 'home.html')

def about(request):
    context = {
        
        "about_page":"active"
        }
    return render(request , 'about.html' , context)


def tracking(request):
    return render(request , 'tracking.html')


def pagenotfound(request):
    return render(request , '404.html')


def thankyou(request):
    return  render(request , 'thank.html')


def offers(request):
    return render(request , 'offers.html')

def terms(request):
    terms = Terms.objects.all()
    context = {
        'terms':terms,
        "about_page":"active"
        }
    return render(request  , 'terms.html',context)