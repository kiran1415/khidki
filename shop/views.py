from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404 , redirect
from .models import Category, Product , ProductOrder
from django.core.mail import send_mail





def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'product_page':'active',
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'category.html', context)

def product_detail(request , id , slug):

    product = get_object_or_404(Product  , id=id , slug=slug  , available=True)
    context = {
        'product_page':'active',
        'product':product
    }
    return render(request , 'single-product.html' , context)


def add_to_cart(request , slug):
    return render(request , 'cart.html')


def order(request , slug):
    product = get_object_or_404(Product  , slug=slug)
    context = {
       'product':product  
    }
    return render(request , 'checkout.html' , context)



def makeorder(request):
    
    if request.method =='POST':
        productname = request.POST['product_name']
        userfirstname = request.POST['first_name']
        userlastname  = request.POST['last_name']
        usercontact = request.POST['phone_number']
        useremail = request.POST['email']
        country = request.POST['country']
        useraddressline1 = request.POST['add_1']
        useraddressline2 = request.POST['add_2']
        city = request.POST['city']
        userpincode = request.POST['zip_code']
        note = request.POST['message']
        
        
        order = ProductOrder.objects.create(productname=productname , userfirstname=userfirstname , userlastname=userlastname , usercontact=usercontact , useremail=useremail , country=country ,useraddressline1 = useraddressline1 , useraddressline2=useraddressline2 , city=city , userpincode=userpincode  , note=note)
        return redirect('/thankyou')
