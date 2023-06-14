from django.shortcuts import render, redirect
from . models import Product,Order, OrderItem
from django.http import JsonResponse
from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from cart.cart import Cart as C
from django.contrib import messages
from django.http import HttpResponseRedirect
from users.models import BillingAdress, Cart ,CartItems
from . forms import BillingAddressForm, CouponForm, CardForm
from django.http import HttpResponseRedirect
from django.views import View
import random

# Create your views here.
def index(request):
    return render(request, 'ecomWeb/home.html', {'products':Product.objects.all()})


def detailpage(request, slug):
    product_ids = []
    product_array = []
    products = Product.objects.all()
    for p in products:
        product_ids.append(p.id)
    
    for i in range(4):
        rn = random.choice(product_ids)
       
        product_array.append(Product.objects.filter(id=rn).exclude(slug=slug))

    return render(request, 'ecomWeb/detail-page.html', {"objects" : Product.objects.filter(slug = slug) , "products" : product_array})


def error_404_view(request, exception):
    return render(request, 'ecomWeb/error.html')

def error_500_view(request):
    return render(request, 'ecomWeb/error.html')





def remove_cart(request, id):
    try:
        cart_item = Cart.objects.get(id = id)
        cart_item.delete()
    except Exception as e:
        print(e)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    

def sunglasses(request):
    context = {
        'offers' : Product.objects.filter(include_offer= True   ),
        'products' : Product.objects.filter(include_offer= False, last_long_product = False, first_long_product = False),
        'long_product_first' : Product.objects.filter(include_offer = False ,first_long_product=True,last_long_product= False),
        'long_product_second' : Product.objects.filter(include_offer = False ,last_long_product=True, first_long_product = False),

    }
    return render(request, 'ecomWeb/glasses/glasses.html',context )

def eyeglasses(request):
    context = {
        'offers' : Product.objects.filter(include_offer= True),
        'products' : Product.objects.filter(include_offer= False, last_long_product = False, first_long_product = False),
        'long_product_first' : Product.objects.filter(include_offer = False ,first_long_product=True,last_long_product= False),
        'long_product_second' : Product.objects.filter(include_offer = False ,last_long_product=True, first_long_product = False),
    }
    return render(request, 'ecomWeb/glasses/glasses.html',context )

def menSunglasses(request):
    context = {
        'products' : Product.objects.filter(include_offer= False, category = 1)
    }
    return render(request, 'ecomWeb/glasses/men.html',context )
     

def womenSunglasses(request):
    context = {
        'products' : Product.objects.filter(include_offer= False, category = 2)
    }
    return render(request, 'ecomWeb/glasses/women.html',context )
     
@login_required(login_url='login')
def cart(request):
    if request.method == 'POST':
        form = CouponForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']

            if code == "ritik":
                messages.success(request, f'Code matched')
            else:
                messages.warning(request, f'Code did not matched.')

            return redirect('cart')
    else:
        form =CouponForm()
    return render(request, 'ecomWeb/cart.html', {'form' : form, 'carts': Cart.objects.filter(is_paid = False, user = request.user)})

def add_to_cart(request, id):
    product = Product.objects.get(id = id)
    user = request.user
    if request.user.is_authenticated:
        cart, _ = Cart.objects.get_or_create(user = user, is_paid = False, product = product)
        cart_items = CartItems.objects.get_or_create(cart = cart, product = product)
        messages.success(request, "Item Added Successfully!")
    else: 
        messages.error(request, f"You have to login in order to add items in cart.")

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def delete_cart(request):
    Cart.objects.all().delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# this view is for the buy now functionality

def buynow(request, id):
    product = Product.objects.get(id = id)
    user = request.user
    if request.user.is_authenticated:
        cart, _ = Cart.objects.get_or_create(user = user, is_paid = False, product = product)
        cart_items = CartItems.objects.get_or_create(cart = cart, product = product)
    else: 
        messages.error(request, f"You have to login in order to add items in cart.")
    return redirect('buy-payout')


@login_required(login_url = 'login')
def buypayout(request):
    cartitems = Cart.objects.filter(user = request.user)
    totalPrice = 0
    for item in cartitems :
        totalPrice = totalPrice+item.product.price
    return render(request, 'ecomWeb/payout/buypayout.html', {  'carts': Cart.objects.filter(is_paid = False, user = request.user) , 'totalprice' : totalPrice})


@login_required(login_url='login')
def placeorder(request):
    if request.method == 'POST':
        neworder = Order()
        neworder.user= request.user
        neworder.fname = request.POST.get('fname')
        neworder.lname = request.POST.get('lname')
        neworder.address = request.POST.get('address')
        neworder.phone = request.POST.get('phone')

        cart = Cart.objects.filter(user = request.user)
        cart_totalPrice = 0
        for item in cart:
            cart_totalPrice += item.product.price 
        neworder.total_price = cart_totalPrice
        # track_number = 'ecomm' + str(random.randint(1111111,9999999))

        # while Order.objects.filter(tracking_no = track_number) in None:
        #     track_number = 'ecomm' + str(random.randint(111111,9999999))
        # neworder.tracking_no = track_number
        neworder.save()

        neworder_items = Cart.objects.filter(user = request.user)
        for item in neworder_items:
            OrderItem.objects.create(
                order = neworder,
                product = item.product,
                price = item.product.price
            )
        
        # to clear user cart objects
        Cart.objects.filter(user = request.user).delete()
        messages.success(request, f"Your order has been placed!")

    return redirect('myorder')        


@login_required(login_url = 'login')
def payout(request):
    cartitems = Cart.objects.filter(user = request.user)
    totalPrice = 0
    for item in cartitems :
        totalPrice = totalPrice+item.product.price
    return render(request, 'ecomWeb/payout/payout.html', {  'carts': Cart.objects.filter(is_paid = False, user = request.user) , 'totalprice' : totalPrice, })


def KhaltiRequestView(request, id):
    card = Carts.objects.get(id= id)
    context = {
        "cart" : cart
    }
    return render(request, 'khaltirequest.html', context)

def offers(request):
    return render(request, 'ecomWeb/offer.html', {"products" : Product.objects.filter(include_offer = True)})


def services(request):
    return render(request, 'ecomWeb/services.html')


class KhaltiVerify(View):

    def get(self,request,*args,**kwargs):
        data = {}
        return JsonResponse(data)