from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404 , redirect
from .models import Category, Product , Liteorder






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
    return render(request , 'order.html' , context)



def makeorder(request):
    
    if request.method =='POST':
        name = request.POST['product_name']
        price  = request.POST['product_price']
        quantity = request.POST['quantity']
        userfirstname = request.POST['userfirst_name']
        userlastname  = request.POST['userlast_name']
        usercontact = request.POST['usercontact']
        useremail = request.POST['useremail']
        userpicode = request.POST['userpincode']
        useraddress = request.POST['useraddress']

        order = Liteorder.objects.create(name=name , price=price , quantity=quantity , userfirstname=userfirstname , userlastname=userlastname , usercontact=usercontact,useremail=useremail ,userpicode=userpicode,useraddress= useraddress)
        return redirect('/thankyou')
def login(request):
    return reverse('accounts:login')