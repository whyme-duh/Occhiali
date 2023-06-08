from django.shortcuts import render, redirect
from . models import Product,Category

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


# Create your views here.
def index(request):
    return render(request, 'ecomWeb/home.html', {'products':Product.objects.all()})


def cart_add(request,id):
    cart =  C(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    messages.success(request, f'Added to cart')
    return redirect("cart")




def remove_cart(request, id):
    try:
        cart_item = Cart.objects.get(id = id)
        cart_item.delete()
    except Exception as e:
        print(e)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    

def sunglasses(request):
    context = {
        'offers' : Product.objects.filter(include_offer= True),
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
    cart, _ = Cart.objects.get_or_create(user = user, is_paid = False, product = product)
    cart_items = CartItems.objects.get_or_create(cart = cart, product = product)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def delete_cart(request):
    Cart.objects.all().delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class ProductDetailView(DetailView):
    template_name = 'ecomWeb/detail-page.html'
    model = Product


@login_required(login_url = 'login')
def payout(request):
    if request.method == 'POST':
        form = BillingAddressForm(request.POST)
        paymentForm = CardForm(request.POST)
        if form.is_vald() or paymentForm.is_valid:
            form.save()
            paymentForm.save()
            messages.success('Payment Done, wait for shipping')
            return redirect('home')
    else:
        form = BillingAddressForm()
        paymentForm = CardForm()
    return render(request, 'ecomWeb/payout/payout.html', {'form': form, 'paymentForm' : paymentForm , 'billing' : BillingAdress.objects.all(), 'carts': Cart.objects.filter(is_paid = False, user = request.user) })

