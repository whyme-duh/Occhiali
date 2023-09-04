from django.shortcuts import render, redirect
from . models import Product,Order, OrderItem
from users. models import Wishlist
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
import requests, json

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
    # if request.method == 'POST':
    #     form = CouponForm(request.POST)
    #     if form.is_valid():
    #         code = form.cleaned_data['code']

    #         if code == "ritik":
    #             messages.success(request, f'Code matched')
    #         else:
    #             messages.warning(request, f'Code did not matched.')

    #         return redirect('cart')
    # else:
    #     form =CouponForm()
    cartitems = Cart.objects.filter(user = request.user)
    delivery_cost, discount = 150, 0
    totalPrice ,itemprice= 0,0
    for item in cartitems :
        itemprice = itemprice + item.product.price 
    totalPrice =itemprice+ delivery_cost - discount
    return render(request, 'ecomWeb/cart.html', { 'carts': Cart.objects.filter(is_paid = False, user = request.user), 'itemprice' : itemprice, 'totalprice' : totalPrice, 'delivery_cost':delivery_cost, 'discount' : discount  })

def add_to_cart(request, id):
    product = Product.objects.get(id = id)
    user = request.user
    if request.user.is_authenticated:
        cart, _ = Cart.objects.get_or_create(user = user, is_paid = False, product = product)
        if product.include_offer:
            product.price = product.discount_price
            product.save()
            cart_items = CartItems.objects.get_or_create(cart = cart, product = product)
        else:
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
    discount, delivery_charge = 0, 150
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
        neworder.total_price = cart_totalPrice + delivery_charge -discount
        neworder.payment_completed = True
        track_number = 'ecomm' + str(random.randint(1111111,9999999))

        while Order.objects.filter(tracking_no = track_number) is None:
            track_number = 'ecomm' + str(random.randint(111111,9999999))
        neworder.tracking_no = track_number
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
        Wishlist.objects.filter(user = request.user).delete()
        messages.success(request, f"Your order has been placed!")

    return redirect('myorder')        


@login_required(login_url = 'login')
def payout(request):
    cartitems = Cart.objects.filter(user = request.user)
    delivery_cost, discount = 150, 0
    totalPrice = 0
    for item in cartitems :
        totalPrice = totalPrice+item.product.price 
    totalPrice += delivery_cost - discount
    return render(request, 'ecomWeb/payout/payout.html', {  'carts': Cart.objects.filter(is_paid = False, user = request.user) , 'totalprice' : totalPrice, 'delivery_cost':delivery_cost, 'discount' : discount  })



def offers(request):
    return render(request, 'ecomWeb/offer.html', {"products" : Product.objects.filter(include_offer = True)})


def services(request):
    return render(request, 'ecomWeb/services.html')




    
def make_payment(request):
    order_id = random.randint(1,19999)
    cartitems = Cart.objects.filter(user = request.user)
    delivery_cost, discount = 150, 0
    totalPrice = 0
    for item in cartitems :
        totalPrice = totalPrice+item.product.price 
    totalPrice =( totalPrice+ delivery_cost - discount)
    khalti_public_key = "test_public_key_93c03d427fc84712a7e39b6bd61d7e23"
    return_url = "http://127.0.0.1:8000/success-payment/"
    url = "https://a.khalti.com/api/v2/epayment/initiate/"

    payload = JsonResponse({
        'public_key' : khalti_public_key,
        "return_url": return_url,
        "website_url": "http://127.0.0.1:8000/home/",
        "amount": totalPrice * 10,
        "purchase_order_id":order_id ,
        "purchase_order_name": "Eyewears",
        
        
        
    })
    headers = {
        'Authorization': 'Key 509023eaf0b847a9b8e529d54758cda8',
        'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    data = response.json()
    print(data)
   
   
    if 'payment_url' in data:
        payment_url = data['payment_url']
        return redirect(payment_url)
   
    else:
        return render(request, 'ecomWeb/error.html')
    

@login_required(login_url='login')
def payment_sucess(request):
   
    status = request.GET.get("status")
    if status == "Completed":
        cartitems = Cart.objects.filter(user = request.user)
        delivery_cost, discount = 150, 0
        totalPrice = 0
        for item in cartitems :
            totalPrice = totalPrice+item.product.price 
        totalPrice += delivery_cost - discount
        return render(request, 'ecomWeb/payout/payment_sucess.html', {'carts': Cart.objects.filter(is_paid = False, user = request.user), 'totalprice' : totalPrice, 'delivery_cost':delivery_cost, 'discount' : discount })
    else:
        return render(request, 'ecomWeb/Error/payment_error.html')




def esewa_payment(request):
    url ="https://uat.esewa.com.np/epay/main"
    d = {'amt': 100,
        'pdc': 0,
        'psc': 0,
        'txAmt': 0,
        'tAmt': 100,
        'pid':'ee2c3ca1-696b-4cc5-a6be-2c40d929d453',
        'scd':'EPAYTEST',
        'su':'http://merchant.com.np/page/esewa_payment_success?q=su',
        'fu':'http://merchant.com.np/page/esewa_payment_failed?q=fu'}
    resp = requests.request("POST",url,data= d)
    if resp.status_code == 200:
        return render(request, 'ecomWeb/payout/payment_sucess.html')
    else:
        return render(request, 'ecomWeb/Error/payment_error.html')


def cancel_order(request, id):
    try:
        cart_item = Order.objects.get(id = id)
        cart_item.delete()
    except Exception as e:
        print(e)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
